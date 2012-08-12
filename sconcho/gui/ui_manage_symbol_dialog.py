# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/manage_symbol_dialog.ui'
#
# Created: Sun Aug 12 11:56:00 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManageKnittingSymbolDialog(object):
    def setupUi(self, ManageKnittingSymbolDialog):
        ManageKnittingSymbolDialog.setObjectName(_fromUtf8("ManageKnittingSymbolDialog"))
        ManageKnittingSymbolDialog.resize(753, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/sconcho_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ManageKnittingSymbolDialog.setWindowIcon(icon)
        self.verticalLayout_5 = QtGui.QVBoxLayout(ManageKnittingSymbolDialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(ManageKnittingSymbolDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.availableSymbolsWidget = QtGui.QTreeWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableSymbolsWidget.sizePolicy().hasHeightForWidth())
        self.availableSymbolsWidget.setSizePolicy(sizePolicy)
        self.availableSymbolsWidget.setColumnCount(1)
        self.availableSymbolsWidget.setObjectName(_fromUtf8("availableSymbolsWidget"))
        self.verticalLayout.addWidget(self.availableSymbolsWidget)
        self.addSymbolButton = QtGui.QPushButton(self.frame)
        self.addSymbolButton.setObjectName(_fromUtf8("addSymbolButton"))
        self.verticalLayout.addWidget(self.addSymbolButton)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.importSymbolsButton = QtGui.QPushButton(self.frame)
        self.importSymbolsButton.setObjectName(_fromUtf8("importSymbolsButton"))
        self.verticalLayout.addWidget(self.importSymbolsButton)
        self.exportSymbolsButton = QtGui.QPushButton(self.frame)
        self.exportSymbolsButton.setObjectName(_fromUtf8("exportSymbolsButton"))
        self.verticalLayout.addWidget(self.exportSymbolsButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.symbolEntryFrame = QtGui.QFrame(ManageKnittingSymbolDialog)
        self.symbolEntryFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.symbolEntryFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.symbolEntryFrame.setObjectName(_fromUtf8("symbolEntryFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.symbolEntryFrame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.symbolEntryFrame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.symbolPreviewFrame = QtGui.QFrame(self.symbolEntryFrame)
        self.symbolPreviewFrame.setMinimumSize(QtCore.QSize(100, 60))
        self.symbolPreviewFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.symbolPreviewFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.symbolPreviewFrame.setObjectName(_fromUtf8("symbolPreviewFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.symbolPreviewFrame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.svgWidget = QSvgWidget(self.symbolPreviewFrame)
        self.svgWidget.setObjectName(_fromUtf8("svgWidget"))
        self.horizontalLayout_2.addWidget(self.svgWidget)
        self.horizontalLayout_8.addWidget(self.symbolPreviewFrame)
        self.svgPathEdit = QtGui.QLineEdit(self.symbolEntryFrame)
        self.svgPathEdit.setReadOnly(False)
        self.svgPathEdit.setObjectName(_fromUtf8("svgPathEdit"))
        self.horizontalLayout_8.addWidget(self.svgPathEdit)
        self.browseSymbolButton = QtGui.QPushButton(self.symbolEntryFrame)
        self.browseSymbolButton.setEnabled(True)
        self.browseSymbolButton.setAutoDefault(False)
        self.browseSymbolButton.setObjectName(_fromUtf8("browseSymbolButton"))
        self.horizontalLayout_8.addWidget(self.browseSymbolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_12 = QtGui.QLabel(self.symbolEntryFrame)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.symbolNameLabel = QtGui.QLabel(self.symbolEntryFrame)
        self.symbolNameLabel.setEnabled(True)
        self.symbolNameLabel.setObjectName(_fromUtf8("symbolNameLabel"))
        self.gridLayout_3.addWidget(self.symbolNameLabel, 0, 0, 1, 1)
        self.symbolNameEntry = QtGui.QLineEdit(self.symbolEntryFrame)
        self.symbolNameEntry.setReadOnly(False)
        self.symbolNameEntry.setObjectName(_fromUtf8("symbolNameEntry"))
        self.gridLayout_3.addWidget(self.symbolNameEntry, 0, 1, 1, 1)
        self.symbolCategoryLabel = QtGui.QLabel(self.symbolEntryFrame)
        self.symbolCategoryLabel.setEnabled(True)
        self.symbolCategoryLabel.setObjectName(_fromUtf8("symbolCategoryLabel"))
        self.gridLayout_3.addWidget(self.symbolCategoryLabel, 1, 0, 1, 1)
        self.symbolWidthLabel = QtGui.QLabel(self.symbolEntryFrame)
        self.symbolWidthLabel.setEnabled(True)
        self.symbolWidthLabel.setObjectName(_fromUtf8("symbolWidthLabel"))
        self.gridLayout_3.addWidget(self.symbolWidthLabel, 3, 0, 1, 1)
        self.symbolWidthSpinner = QtGui.QSpinBox(self.symbolEntryFrame)
        self.symbolWidthSpinner.setEnabled(True)
        self.symbolWidthSpinner.setReadOnly(False)
        self.symbolWidthSpinner.setMinimum(1)
        self.symbolWidthSpinner.setObjectName(_fromUtf8("symbolWidthSpinner"))
        self.gridLayout_3.addWidget(self.symbolWidthSpinner, 3, 1, 1, 1)
        self.symbolDescriptionLabel = QtGui.QLabel(self.symbolEntryFrame)
        self.symbolDescriptionLabel.setEnabled(True)
        self.symbolDescriptionLabel.setObjectName(_fromUtf8("symbolDescriptionLabel"))
        self.gridLayout_3.addWidget(self.symbolDescriptionLabel, 4, 0, 1, 1)
        self.symbolDescriptionEntry = QtGui.QTextEdit(self.symbolEntryFrame)
        self.symbolDescriptionEntry.setReadOnly(False)
        self.symbolDescriptionEntry.setObjectName(_fromUtf8("symbolDescriptionEntry"))
        self.gridLayout_3.addWidget(self.symbolDescriptionEntry, 4, 1, 1, 1)
        self.categoryChooser = QtGui.QComboBox(self.symbolEntryFrame)
        self.categoryChooser.setObjectName(_fromUtf8("categoryChooser"))
        self.gridLayout_3.addWidget(self.categoryChooser, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cancelOrDeleteButton = QtGui.QPushButton(self.symbolEntryFrame)
        self.cancelOrDeleteButton.setObjectName(_fromUtf8("cancelOrDeleteButton"))
        self.horizontalLayout_3.addWidget(self.cancelOrDeleteButton)
        self.addOrUpdateButton = QtGui.QPushButton(self.symbolEntryFrame)
        self.addOrUpdateButton.setObjectName(_fromUtf8("addOrUpdateButton"))
        self.horizontalLayout_3.addWidget(self.addOrUpdateButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.symbolEntryFrame)
        spacerItem3 = QtGui.QSpacerItem(13, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.pushButton_4 = QtGui.QPushButton(ManageKnittingSymbolDialog)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.symbolNameLabel.setBuddy(self.symbolNameEntry)
        self.symbolCategoryLabel.setBuddy(self.categoryChooser)
        self.symbolWidthLabel.setBuddy(self.symbolWidthSpinner)
        self.symbolDescriptionLabel.setBuddy(self.symbolDescriptionEntry)

        self.retranslateUi(ManageKnittingSymbolDialog)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageKnittingSymbolDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ManageKnittingSymbolDialog)

    def retranslateUi(self, ManageKnittingSymbolDialog):
        ManageKnittingSymbolDialog.setWindowTitle(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "sconcho: Manage Custom Knitting Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Available Symbols</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.availableSymbolsWidget.headerItem().setText(0, QtGui.QApplication.translate("ManageKnittingSymbolDialog", "Category/Symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.addSymbolButton.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "&Add New Symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.importSymbolsButton.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "Import Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.exportSymbolsButton.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "Export Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">SVG Image</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.browseSymbolButton.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Description</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.symbolNameLabel.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "symbol &name", None, QtGui.QApplication.UnicodeUTF8))
        self.symbolCategoryLabel.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "symbol &category", None, QtGui.QApplication.UnicodeUTF8))
        self.symbolWidthLabel.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "symbol &width", None, QtGui.QApplication.UnicodeUTF8))
        self.symbolDescriptionLabel.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "symbol &description", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelOrDeleteButton.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.addOrUpdateButton.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("ManageKnittingSymbolDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.QtSvg import QSvgWidget
