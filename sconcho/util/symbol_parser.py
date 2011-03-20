# -*- coding: utf-8 -*-
########################################################################
#
# (c) 2010 Markus Dittrich
#
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public
# License Version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License Version 3 for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
#
#######################################################################

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from PyQt4.QtCore import (QDir, QFile, QString, QStringList, QIODevice,
                          QTextStream, QTemporaryFile, Qt)
from PyQt4.QtGui import QMessageBox
from PyQt4.QtXml import QDomDocument

from sconcho.util.misc import errorLogger
import sconcho.util.messages as msg


# need this for sorting symbol entries
# at the end of the category list
__LARGE_INT__ = 100000



def parse_all_symbols(symbolTopLevelPaths):
    """ 
    This function reads all available knitting symbols and
    returns a dictionary with them all.
    """

    symbolPaths = get_list_of_symbol_paths(symbolTopLevelPaths)

    allSymbolDesc = {}
    for path in symbolPaths:
        symbolDesc = parse_knitting_symbol(path)
        
        # if there was a problem we simply skip
        # with a short warning
        if not symbolDesc:
            errorLogger.write("parse_all_symbols: Could not read symbol "
                              + path)
            continue

        # try to add symbol to symbol database
        try:
            symbolID = symbolDesc["name"] 
            allSymbolDesc[symbolID] = symbolDesc
        except KeyError:
            continue

    return allSymbolDesc



def get_list_of_symbol_paths(symbolTopLevelPaths):
    """
    Given a list of top level paths to directories containting
    sconcho kitting symbols returns a QStringList of all paths to 
    individual sconcho patterns.
    """

    symbolPaths = []
    for path in symbolTopLevelPaths:
        aDir = QDir(path)
        for entry in aDir.entryList(QDir.AllDirs | QDir.NoDotAndDotDot):
            symbolPaths.append(aDir.absolutePath() + "/" + entry)

    return symbolPaths
        


def parse_knitting_symbol(symbolPath):
    """
    Parse the knitting symbol located at path symbolPath.
    """

    descriptionFile = QFile(symbolPath + "/description")
    if (not descriptionFile.exists()) or descriptionFile.error():
        return None

    # parse XML
    dom = QDomDocument()
    (status, msg, line, col) = dom.setContent(descriptionFile)
    if not status:
        errorMessage = ("Failed reading pattern description in file %s -- "
                        "%s at line %d column %d" % 
                        (descriptionFile.fileName(), msg, line, col))
        errorLogger.write(errorMessage)
        return None

    # make sure we're reading a sconcho pattern description 
    root = dom.documentElement()
    if root.tagName() != "sconcho":
        return None

    # parse the actual content
    node = root.firstChild()
    if node.toElement().tagName() != "knittingSymbol":
        return None
  
    content = parse_symbol_description(node)

    # add the absolute path
    content["svgPath"] = symbolPath + "/" + content["svgName"] + ".svg"

    return content



def parse_symbol_description(node):
    """
    Parses the main content of a sconcho pattern description
    file. 
    FIXME: This function currently does not much checking 
           and probably should do more.
    """

    content = {}

    item = node.firstChild()
    while not item.isNull():

        #entry = item.firstChild().toText().data()
        entry = item.firstChild().toCharacterData().data()

        if item.toElement().tagName() == "svgName":
            content["svgName"] = entry

        # looks like we explicitly have to copy the QStringList
        # elements into a QString otherwise the code seg faults
        if item.toElement().tagName() == "category":
            splitEntry = entry.split(":")
            if len(splitEntry) == 1:
                content["category"] = QString(splitEntry.first())
                content["category_pos"] = QString("%d" % __LARGE_INT__)
            elif len(splitEntry) == 2:
                content["category"] = QString(splitEntry.first())
                content["category_pos"] = QString(splitEntry.last())
            else:
                return None


        if item.toElement().tagName() == "symbolName":
            content["name"] = entry

        if item.toElement().tagName() == "symbolDescription":
            content["description"] = entry

        if item.toElement().tagName() == "symbolWidth":
            content["width"] = entry

        if item.toElement().tagName() == "backgroundColor":
            content["backgroundColor"] = entry

        item = item.nextSibling();

    return content



def create_new_symbol(symbolPath, svgPath, svgName, category, name, 
                      description, width):
    """ This function creates a new knitting symbol as specified by
    the user. 
    """

    # make sure the user's symbol directory exists. If not we
    # create it
    symbolTopDir = QDir(symbolPath)
    if not symbolTopDir.exists():
        if not symbolTopDir.mkdir(symbolPath):
            QMessageBox.critical(None, msg.failedToCreateDirectoryTitle,
                                 msg.failedToCreateDirectoryText % symbolPath,
                                 QMessageBox.Close)
            return False

    # this should never happen since the manageKnittingSymbolDialog is
    # supposed to check. We'll check anyways.
    symbolDirPath = symbolPath + "/" + svgName
    symbolDir = QDir(symbolDirPath)
    if symbolDir.exists():
        QMessageBox.critical(None, msg.symbolExistsTitle,
                             msg.symbolExistsText % (category, name),
                             QMessageBox.Close)
        return False

    symbolDir.mkdir(symbolDirPath)

    # the following try/except suite attempts to return things back
    # to the initial state if writing fails for some reason
    descriptionFileHandle = None
    symbolTargetFilePath  = None

    try:
        
        # copy the svg file
        symbolTargetFilePath = symbolDirPath + "/" + svgName + ".svg"
        if not QFile(svgPath).copy(symbolTargetFilePath):
            QMessageBox.critical(None, msg.failedToCopySvgTitle,
                                msg.failedToCopySvgText % symbolTargetFilePath,
                                QMessageBox.Close)
           
            raise IOError

        # write the description file
        descriptionFileHandle = QFile(symbolDirPath + "/" + "description")
        if not descriptionFileHandle.open(QIODevice.WriteOnly):
            QMessageBox.critical(None, msg.failedToCreateDescriptionFIleTitle,
                                msg.failedToCreateDescriptionFileText % (category,
                                name), QMessageBox.Close)
            raise IOError

        # finally try to write the content of the file
        try:
            write_description_content(descriptionFileHandle, svgName, category, 
                                      name, description, width)
        except:
            raise IOError

    except IOError:
        if descriptionFileHandle:
            symbolDir.remove(descriptionFileHandle)

        if symbolTargetFilePath:
            symbolDir.remove(symbolTargetFilePath)

        symbolDir.remove(symbolDirPath)
        return False

    return True



def write_description_content(handle, svgName, category, name, description,
                              width):
    """ This function generates the xml content of the description 
    file.
    """
    
    stream = QTextStream(handle)
    stream.setCodec("UTF-8")
    stream << ("<?xml version='1.0' encoding='UTF-8'?>\n"
               "<sconcho>\n"
               "  <knittingSymbol>\n"
               "    <svgName>%s</svgName>\n"
               "    <category>%s</category>\n"
               "    <symbolName>%s</symbolName>\n"
               "    <symbolDescription>%s</symbolDescription>\n"
               "    <symbolWidth>%d</symbolWidth>\n"
               "  </knittingSymbol>\n"
               "</sconcho>\n"
               % (Qt.escape(svgName), Qt.escape(category), Qt.escape(name), 
                  Qt.escape(description), width))



def remove_symbol(symbolTopPath, name):
    """ This function removes the symbol named name from the
    database located at symbolPath.
    """

    symbolPath = symbolTopPath + "/" + name
    symbolPathDir = QDir(symbolPath)
    if not symbolPathDir.exists():
       return False

    descriptionFile = symbolPath + "/description"
    svgFile         = symbolPath + "/" + name + ".svg"

    if symbolPathDir.remove(descriptionFile):
        if symbolPathDir.remove(svgFile):
            if symbolPathDir.rmdir(symbolPath):
                return True

    return False



def move_symbol(oldPath, newPath):
    """ Move the the symbol at oldPath to newPath. 
    The function returns True on success and False otherwise.
    """

    symOldDir = QDir(oldPath)
    symNewDir = QDir(newPath)
    if symOldDir.exists():
        if not symNewDir.exists():
            return symNewDir.rename(oldPath, newPath)

    return False



def remove_directory(path):
    """ Removes the directory at path. """

    deadDir = QDir(path)
    return deadDir.rmdir(path)
