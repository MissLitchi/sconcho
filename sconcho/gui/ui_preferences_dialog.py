# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/preferences_dialog.ui'
#
# Created: Sat Sep 24 13:25:43 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName(_fromUtf8("PreferencesDialog"))
        PreferencesDialog.resize(480, 514)
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "sconcho: Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_8 = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.legendTab = QtGui.QWidget()
        self.legendTab.setObjectName(_fromUtf8("legendTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.legendTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.legendTab)
        self.groupBox.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Legend Font", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("PreferencesDialog", "Family", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.legendFontComboBox = QtGui.QFontComboBox(self.groupBox)
        self.legendFontComboBox.setObjectName(_fromUtf8("legendFontComboBox"))
        self.gridLayout.addWidget(self.legendFontComboBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("PreferencesDialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.legendStyleComboBox = QtGui.QComboBox(self.groupBox)
        self.legendStyleComboBox.setObjectName(_fromUtf8("legendStyleComboBox"))
        self.gridLayout.addWidget(self.legendStyleComboBox, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("PreferencesDialog", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.legendSizeComboBox = QtGui.QComboBox(self.groupBox)
        self.legendSizeComboBox.setObjectName(_fromUtf8("legendSizeComboBox"))
        self.gridLayout.addWidget(self.legendSizeComboBox, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.legendExampleText = QtGui.QLineEdit(self.groupBox)
        self.legendExampleText.setObjectName(_fromUtf8("legendExampleText"))
        self.verticalLayout_4.addWidget(self.legendExampleText)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 74, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.legendTab, _fromUtf8(""))
        self.labelTab = QtGui.QWidget()
        self.labelTab.setObjectName(_fromUtf8("labelTab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.labelTab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox_2 = QtGui.QGroupBox(self.labelTab)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Label Font", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setText(QtGui.QApplication.translate("PreferencesDialog", "Family", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.labelFontComboBox = QtGui.QFontComboBox(self.groupBox_2)
        self.labelFontComboBox.setObjectName(_fromUtf8("labelFontComboBox"))
        self.gridLayout_3.addWidget(self.labelFontComboBox, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setText(QtGui.QApplication.translate("PreferencesDialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.labelStyleComboBox = QtGui.QComboBox(self.groupBox_2)
        self.labelStyleComboBox.setObjectName(_fromUtf8("labelStyleComboBox"))
        self.gridLayout_3.addWidget(self.labelStyleComboBox, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setText(QtGui.QApplication.translate("PreferencesDialog", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.labelSizeComboBox = QtGui.QComboBox(self.groupBox_2)
        self.labelSizeComboBox.setObjectName(_fromUtf8("labelSizeComboBox"))
        self.gridLayout_3.addWidget(self.labelSizeComboBox, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.labelExampleText = QtGui.QLineEdit(self.groupBox_2)
        self.labelExampleText.setObjectName(_fromUtf8("labelExampleText"))
        self.verticalLayout_5.addWidget(self.labelExampleText)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.labelTab)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Row Label Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.showEvenRowsButton = QtGui.QRadioButton(self.groupBox_3)
        self.showEvenRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Even Row Labels Only", None, QtGui.QApplication.UnicodeUTF8))
        self.showEvenRowsButton.setObjectName(_fromUtf8("showEvenRowsButton"))
        self.buttonGroup = QtGui.QButtonGroup(PreferencesDialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.showEvenRowsButton)
        self.gridLayout_6.addWidget(self.showEvenRowsButton, 7, 0, 1, 1)
        self.labelOddRowsButton = QtGui.QRadioButton(self.groupBox_3)
        self.labelOddRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Hide Even Row Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOddRowsButton.setObjectName(_fromUtf8("labelOddRowsButton"))
        self.buttonGroup.addButton(self.labelOddRowsButton)
        self.gridLayout_6.addWidget(self.labelOddRowsButton, 3, 0, 1, 1)
        self.labelAllRowsButton = QtGui.QRadioButton(self.groupBox_3)
        self.labelAllRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Label All Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAllRowsButton.setChecked(True)
        self.labelAllRowsButton.setObjectName(_fromUtf8("labelAllRowsButton"))
        self.buttonGroup.addButton(self.labelAllRowsButton)
        self.gridLayout_6.addWidget(self.labelAllRowsButton, 2, 0, 1, 1)
        self.labelEvenRowsButton = QtGui.QRadioButton(self.groupBox_3)
        self.labelEvenRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Hide Odd Row Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEvenRowsButton.setObjectName(_fromUtf8("labelEvenRowsButton"))
        self.buttonGroup.addButton(self.labelEvenRowsButton)
        self.gridLayout_6.addWidget(self.labelEvenRowsButton, 4, 0, 1, 1)
        self.showOddRowsButton = QtGui.QRadioButton(self.groupBox_3)
        self.showOddRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Odd Row Labels Only", None, QtGui.QApplication.UnicodeUTF8))
        self.showOddRowsButton.setObjectName(_fromUtf8("showOddRowsButton"))
        self.buttonGroup.addButton(self.showOddRowsButton)
        self.gridLayout_6.addWidget(self.showOddRowsButton, 6, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setText(QtGui.QApplication.translate("PreferencesDialog", "row labels start at", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 2, 2, 1, 1)
        self.rowLabelStartSpinner = QtGui.QSpinBox(self.groupBox_3)
        self.rowLabelStartSpinner.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rowLabelStartSpinner.setMinimum(1)
        self.rowLabelStartSpinner.setMaximum(10000)
        self.rowLabelStartSpinner.setObjectName(_fromUtf8("rowLabelStartSpinner"))
        self.gridLayout_6.addWidget(self.rowLabelStartSpinner, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.labelTab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(20, 46, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setText(QtGui.QApplication.translate("PreferencesDialog", "Grid Cell Width (pixels)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridCellWidthSpinner = QtGui.QSpinBox(self.tab_2)
        self.gridCellWidthSpinner.setMinimum(1)
        self.gridCellWidthSpinner.setMaximum(1000)
        self.gridCellWidthSpinner.setObjectName(_fromUtf8("gridCellWidthSpinner"))
        self.gridLayout_2.addWidget(self.gridCellWidthSpinner, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setText(QtGui.QApplication.translate("PreferencesDialog", "Grid Cell Height (pixels)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridCellHeightSpinner = QtGui.QSpinBox(self.tab_2)
        self.gridCellHeightSpinner.setMinimum(1)
        self.gridCellHeightSpinner.setMaximum(1000)
        self.gridCellHeightSpinner.setObjectName(_fromUtf8("gridCellHeightSpinner"))
        self.gridLayout_2.addWidget(self.gridCellHeightSpinner, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 128, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.oddRowHighlightCheck = QtGui.QCheckBox(self.tab_2)
        self.oddRowHighlightCheck.setText(QtGui.QApplication.translate("PreferencesDialog", "Highlight Odd Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.oddRowHighlightCheck.setObjectName(_fromUtf8("oddRowHighlightCheck"))
        self.gridLayout_4.addWidget(self.oddRowHighlightCheck, 0, 0, 1, 1)
        self.oddRowHighlightColorButton = QtGui.QPushButton(self.tab_2)
        self.oddRowHighlightColorButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Highlight Color", None, QtGui.QApplication.UnicodeUTF8))
        self.oddRowHighlightColorButton.setAutoDefault(False)
        self.oddRowHighlightColorButton.setObjectName(_fromUtf8("oddRowHighlightColorButton"))
        self.gridLayout_4.addWidget(self.oddRowHighlightColorButton, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setText(QtGui.QApplication.translate("PreferencesDialog", "&Opacity (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.oddRowHighlightOpacitySpinner = QtGui.QSpinBox(self.tab_2)
        self.oddRowHighlightOpacitySpinner.setMaximum(100)
        self.oddRowHighlightOpacitySpinner.setObjectName(_fromUtf8("oddRowHighlightOpacitySpinner"))
        self.gridLayout_4.addWidget(self.oddRowHighlightOpacitySpinner, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setText(QtGui.QApplication.translate("PreferencesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Location of Custom Knitting Symbols</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.customSymbolPathEdit = QtGui.QLineEdit(self.tab)
        self.customSymbolPathEdit.setObjectName(_fromUtf8("customSymbolPathEdit"))
        self.horizontalLayout_2.addWidget(self.customSymbolPathEdit)
        self.customSymbolPathButton = QtGui.QPushButton(self.tab)
        self.customSymbolPathButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.customSymbolPathButton.setAutoDefault(False)
        self.customSymbolPathButton.setObjectName(_fromUtf8("customSymbolPathButton"))
        self.horizontalLayout_2.addWidget(self.customSymbolPathButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 185, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_8.addWidget(self.tabWidget)
        spacerItem5 = QtGui.QSpacerItem(20, 236, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.makeDefaultButton = QtGui.QPushButton(PreferencesDialog)
        self.makeDefaultButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Make &Default", None, QtGui.QApplication.UnicodeUTF8))
        self.makeDefaultButton.setAutoDefault(False)
        self.makeDefaultButton.setObjectName(_fromUtf8("makeDefaultButton"))
        self.horizontalLayout.addWidget(self.makeDefaultButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton = QtGui.QPushButton(PreferencesDialog)
        self.pushButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.label_7.setBuddy(self.oddRowHighlightOpacitySpinner)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PreferencesDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.legendTab), QtGui.QApplication.translate("PreferencesDialog", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.labelTab), QtGui.QApplication.translate("PreferencesDialog", "Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("PreferencesDialog", "Grid Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PreferencesDialog", "Custom Symbol Location", None, QtGui.QApplication.UnicodeUTF8))

