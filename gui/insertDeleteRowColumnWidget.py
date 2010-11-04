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

from PyQt4.QtCore import (Qt, SIGNAL, QString)
from PyQt4.QtGui import QDialog
from gui.ui_insertDeleteRowColumnWidget import Ui_InsertDeleteRowColumnWidget



##########################################################################
#
# This widget provides a dialog for inserting and deleting rows
# of the main pattern grid.
#
##########################################################################
class InsertDeleteRowColumnWidget(QDialog, Ui_InsertDeleteRowColumnWidget):


    def __init__(self, numRows, numCols, row, col, parent = None):
        """
        Initialize the dialog.
        """

        super(InsertDeleteRowColumnWidget, self).__init__(parent)
        self.setupUi(self)

        # set the maximum of the spinbox
        self.set_upper_row_limit(numRows)
        self.set_upper_column_limit(numCols)

        # set the current values for row/column to be changed
        self.set_row_col(row, col)

        # install some connections
        self.connect(self.closeButton, SIGNAL("clicked()"), self.close)
        self.connect(self.insertRowButton, SIGNAL("clicked()"),
                     self.insert_row_button_pressed)
        self.connect(self.deleteRowButton, SIGNAL("clicked()"),
                     self.delete_row_button_pressed)
        self.connect(self.insertColumnButton, SIGNAL("clicked()"),
                     self.insert_column_button_pressed)
        self.connect(self.deleteColumnButton, SIGNAL("clicked()"),
                     self.delete_column_button_pressed)



    def insert_row_button_pressed(self):
        """
        This method forwards clicks on the insertRowButton.
        """

        numRows    = self.numInsertRows.value()
        pivot      = self.insertRowPivot.value()
        insertMode = self.insertRowMode.currentText()

        if pivot <= 0:
            return

        self.emit(SIGNAL("insert_row"), numRows, insertMode, pivot)
        
        
        
    def delete_row_button_pressed(self):
        """
        This method forwards clicks on the deleteRowButton.
        """

        deadRowID = self.deleteRowID.value()

        if deadRowID <= 0:
            return

        self.emit(SIGNAL("delete_row"), deadRowID)



    def insert_column_button_pressed(self):
        """
        This method forwards clicks on the insertColumnButton.
        """
        
        numColumns = self.numInsertColumns.value()
        pivot      = self.insertColumnPivot.value()
        insertMode = self.insertColumnMode.currentText()

        if pivot <= 0:
            return

        self.emit(SIGNAL("insert_column"), numColumns, insertMode, pivot)



    def delete_column_button_pressed(self):
        """
        This method forwards clicks on the deleteColumnButton.
        """

        deadColumnID = self.deleteColumnID.value()

        if deadColumnID <=0:
            return

        self.emit(SIGNAL("delete_column"), deadColumnID)
        


    def set_upper_row_limit(self, numRows):
        """
        Sets the upper limit of the row selectors based
        on the number of available rows.
        """

        self.insertRowPivot.setMinimum(1)
        self.insertRowPivot.setMaximum(numRows)
        self.deleteRowID.setMinimum(1)
        self.deleteRowID.setMaximum(numRows)
        self.__numRows = numRows
        


    def set_upper_column_limit(self, numCols):
        """
        Sets the upper limit of the column selectors based
        on the number of available columns.
        """
        
        self.insertColumnPivot.setMinimum(1)
        self.insertColumnPivot.setMaximum(numCols)
        self.deleteColumnID.setMinimum(1)
        self.deleteColumnID.setMaximum(numCols)
        self.__numCols = numCols


    def row_col_count_changed(self, type, num):
        """
        Adjusts the row and column limits.
        """

        if type == "numRows":
            self.set_upper_row_limit(num)
        elif type == "numColumns":
            self.set_upper_column_limit(num)
        else:
            print("Error: asked to adjust ", type, " which is unknown.")


    def set_row_col(self, row, col):
        """ Set the current value of row/column entry to
        be changed.
        """

        self.insertRowPivot.setValue(self.__numRows - row)
        self.insertColumnPivot.setValue(self.__numCols - col)
