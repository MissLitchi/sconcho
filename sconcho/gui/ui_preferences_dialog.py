# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/preferences_dialog.ui'
#
# Created: Sat Aug 11 17:04:29 2012
#      by: PyQt4 UI code generator 4.9.1
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
        PreferencesDialog.resize(614, 702)
        self.verticalLayout_10 = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.legendTab = QtGui.QWidget()
        self.legendTab.setObjectName(_fromUtf8("legendTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.legendTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.legendTab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.legendFontComboBox = QtGui.QFontComboBox(self.groupBox)
        self.legendFontComboBox.setObjectName(_fromUtf8("legendFontComboBox"))
        self.gridLayout.addWidget(self.legendFontComboBox, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.legendStyleComboBox = QtGui.QComboBox(self.groupBox)
        self.legendStyleComboBox.setObjectName(_fromUtf8("legendStyleComboBox"))
        self.gridLayout.addWidget(self.legendStyleComboBox, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
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
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.labelTab)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.groupBox_2 = QtGui.QGroupBox(self.labelTab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.labelFontComboBox = QtGui.QFontComboBox(self.groupBox_2)
        self.labelFontComboBox.setObjectName(_fromUtf8("labelFontComboBox"))
        self.gridLayout_3.addWidget(self.labelFontComboBox, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.labelStyleComboBox = QtGui.QComboBox(self.groupBox_2)
        self.labelStyleComboBox.setObjectName(_fromUtf8("labelStyleComboBox"))
        self.gridLayout_3.addWidget(self.labelStyleComboBox, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
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
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.showRowLabelChecker = QtGui.QGroupBox(self.labelTab)
        self.showRowLabelChecker.setCheckable(True)
        self.showRowLabelChecker.setObjectName(_fromUtf8("showRowLabelChecker"))
        self.verticalLayout = QtGui.QVBoxLayout(self.showRowLabelChecker)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.customRowLabelsChecker = QtGui.QCheckBox(self.showRowLabelChecker)
        self.customRowLabelsChecker.setObjectName(_fromUtf8("customRowLabelsChecker"))
        self.verticalLayout.addWidget(self.customRowLabelsChecker)
        self.line_2 = QtGui.QFrame(self.showRowLabelChecker)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_9 = QtGui.QLabel(self.showRowLabelChecker)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.evenRowLabelLocationComboBox = QtGui.QComboBox(self.showRowLabelChecker)
        self.evenRowLabelLocationComboBox.setObjectName(_fromUtf8("evenRowLabelLocationComboBox"))
        self.evenRowLabelLocationComboBox.addItem(_fromUtf8(""))
        self.evenRowLabelLocationComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.evenRowLabelLocationComboBox)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 5, 0, 1, 3)
        self.showRowsWithIntervalButton = QtGui.QRadioButton(self.showRowLabelChecker)
        self.showRowsWithIntervalButton.setObjectName(_fromUtf8("showRowsWithIntervalButton"))
        self.buttonGroup = QtGui.QButtonGroup(PreferencesDialog)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.showRowsWithIntervalButton)
        self.gridLayout_5.addWidget(self.showRowsWithIntervalButton, 3, 0, 1, 1)
        self.showOddRowsButton = QtGui.QRadioButton(self.showRowLabelChecker)
        self.showOddRowsButton.setObjectName(_fromUtf8("showOddRowsButton"))
        self.buttonGroup.addButton(self.showOddRowsButton)
        self.gridLayout_5.addWidget(self.showOddRowsButton, 1, 0, 1, 2)
        self.rowLabelsIntervalSpinner = QtGui.QSpinBox(self.showRowLabelChecker)
        self.rowLabelsIntervalSpinner.setMinimum(1)
        self.rowLabelsIntervalSpinner.setMaximum(10000)
        self.rowLabelsIntervalSpinner.setObjectName(_fromUtf8("rowLabelsIntervalSpinner"))
        self.gridLayout_5.addWidget(self.rowLabelsIntervalSpinner, 3, 1, 1, 1)
        self.rowLabelsIntervalStartSpinner = QtGui.QSpinBox(self.showRowLabelChecker)
        self.rowLabelsIntervalStartSpinner.setMinimum(-10000)
        self.rowLabelsIntervalStartSpinner.setMaximum(10000)
        self.rowLabelsIntervalStartSpinner.setProperty("value", 1)
        self.rowLabelsIntervalStartSpinner.setObjectName(_fromUtf8("rowLabelsIntervalStartSpinner"))
        self.gridLayout_5.addWidget(self.rowLabelsIntervalStartSpinner, 3, 3, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_13 = QtGui.QLabel(self.showRowLabelChecker)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_6.addWidget(self.label_13)
        self.oddRowLabelLocationComboBox = QtGui.QComboBox(self.showRowLabelChecker)
        self.oddRowLabelLocationComboBox.setObjectName(_fromUtf8("oddRowLabelLocationComboBox"))
        self.oddRowLabelLocationComboBox.addItem(_fromUtf8(""))
        self.oddRowLabelLocationComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.oddRowLabelLocationComboBox)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 4, 0, 1, 3)
        self.showEvenRowsButton = QtGui.QRadioButton(self.showRowLabelChecker)
        self.showEvenRowsButton.setObjectName(_fromUtf8("showEvenRowsButton"))
        self.buttonGroup.addButton(self.showEvenRowsButton)
        self.gridLayout_5.addWidget(self.showEvenRowsButton, 2, 0, 1, 2)
        self.rowLabelsStartLabel = QtGui.QLabel(self.showRowLabelChecker)
        self.rowLabelsStartLabel.setObjectName(_fromUtf8("rowLabelsStartLabel"))
        self.gridLayout_5.addWidget(self.rowLabelsStartLabel, 3, 2, 1, 1)
        self.labelAllRowsButton = QtGui.QRadioButton(self.showRowLabelChecker)
        self.labelAllRowsButton.setChecked(True)
        self.labelAllRowsButton.setObjectName(_fromUtf8("labelAllRowsButton"))
        self.buttonGroup.addButton(self.labelAllRowsButton)
        self.gridLayout_5.addWidget(self.labelAllRowsButton, 0, 0, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_8 = QtGui.QLabel(self.showRowLabelChecker)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_7.addWidget(self.label_8)
        self.rowLabelStartSpinner = QtGui.QSpinBox(self.showRowLabelChecker)
        self.rowLabelStartSpinner.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rowLabelStartSpinner.setMinimum(-10000)
        self.rowLabelStartSpinner.setMaximum(10000)
        self.rowLabelStartSpinner.setObjectName(_fromUtf8("rowLabelStartSpinner"))
        self.horizontalLayout_7.addWidget(self.rowLabelStartSpinner)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout_9.addWidget(self.showRowLabelChecker)
        self.showColumnLabelChecker = QtGui.QGroupBox(self.labelTab)
        self.showColumnLabelChecker.setCheckable(True)
        self.showColumnLabelChecker.setObjectName(_fromUtf8("showColumnLabelChecker"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.showColumnLabelChecker)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.customColumnLabelsChecker = QtGui.QCheckBox(self.showColumnLabelChecker)
        self.customColumnLabelsChecker.setObjectName(_fromUtf8("customColumnLabelsChecker"))
        self.verticalLayout_7.addWidget(self.customColumnLabelsChecker)
        self.line_3 = QtGui.QFrame(self.showColumnLabelChecker)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_7.addWidget(self.line_3)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.labelAllColumnsButton = QtGui.QRadioButton(self.showColumnLabelChecker)
        self.labelAllColumnsButton.setChecked(True)
        self.labelAllColumnsButton.setObjectName(_fromUtf8("labelAllColumnsButton"))
        self.gridLayout_6.addWidget(self.labelAllColumnsButton, 0, 0, 1, 1)
        self.showColumnsWithIntervalButton = QtGui.QRadioButton(self.showColumnLabelChecker)
        self.showColumnsWithIntervalButton.setObjectName(_fromUtf8("showColumnsWithIntervalButton"))
        self.gridLayout_6.addWidget(self.showColumnsWithIntervalButton, 1, 0, 1, 1)
        self.columnLabelsIntervalSpinner = QtGui.QSpinBox(self.showColumnLabelChecker)
        self.columnLabelsIntervalSpinner.setMinimum(1)
        self.columnLabelsIntervalSpinner.setMaximum(10000)
        self.columnLabelsIntervalSpinner.setObjectName(_fromUtf8("columnLabelsIntervalSpinner"))
        self.gridLayout_6.addWidget(self.columnLabelsIntervalSpinner, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.showColumnLabelChecker)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_6.addWidget(self.label_16, 1, 2, 1, 1)
        self.columnLabelsIntervalStartSpinner = QtGui.QSpinBox(self.showColumnLabelChecker)
        self.columnLabelsIntervalStartSpinner.setMinimum(1)
        self.columnLabelsIntervalStartSpinner.setMaximum(10000)
        self.columnLabelsIntervalStartSpinner.setObjectName(_fromUtf8("columnLabelsIntervalStartSpinner"))
        self.gridLayout_6.addWidget(self.columnLabelsIntervalStartSpinner, 1, 3, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_6)
        self.verticalLayout_9.addWidget(self.showColumnLabelChecker)
        self.tabWidget.addTab(self.labelTab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridCellWidthSpinner = QtGui.QSpinBox(self.tab_2)
        self.gridCellWidthSpinner.setMinimum(1)
        self.gridCellWidthSpinner.setMaximum(1000)
        self.gridCellWidthSpinner.setObjectName(_fromUtf8("gridCellWidthSpinner"))
        self.gridLayout_2.addWidget(self.gridCellWidthSpinner, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridCellHeightSpinner = QtGui.QSpinBox(self.tab_2)
        self.gridCellHeightSpinner.setMinimum(1)
        self.gridCellHeightSpinner.setMaximum(1000)
        self.gridCellHeightSpinner.setObjectName(_fromUtf8("gridCellHeightSpinner"))
        self.gridLayout_2.addWidget(self.gridCellHeightSpinner, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem3)
        self.rowHighlightChecker = QtGui.QGroupBox(self.tab_2)
        self.rowHighlightChecker.setCheckable(True)
        self.rowHighlightChecker.setObjectName(_fromUtf8("rowHighlightChecker"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.rowHighlightChecker)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_7 = QtGui.QLabel(self.rowHighlightChecker)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 3, 0, 1, 1)
        self.highlightRowOpacitySpinner = QtGui.QSpinBox(self.rowHighlightChecker)
        self.highlightRowOpacitySpinner.setMaximum(100)
        self.highlightRowOpacitySpinner.setObjectName(_fromUtf8("highlightRowOpacitySpinner"))
        self.gridLayout_4.addWidget(self.highlightRowOpacitySpinner, 3, 1, 1, 1)
        self.highlightRowColorButton = QtGui.QPushButton(self.rowHighlightChecker)
        self.highlightRowColorButton.setAutoDefault(False)
        self.highlightRowColorButton.setObjectName(_fromUtf8("highlightRowColorButton"))
        self.gridLayout_4.addWidget(self.highlightRowColorButton, 1, 0, 1, 1)
        self.highlightRowStartComboBox = QtGui.QComboBox(self.rowHighlightChecker)
        self.highlightRowStartComboBox.setObjectName(_fromUtf8("highlightRowStartComboBox"))
        self.highlightRowStartComboBox.addItem(_fromUtf8(""))
        self.highlightRowStartComboBox.addItem(_fromUtf8(""))
        self.gridLayout_4.addWidget(self.highlightRowStartComboBox, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.verticalLayout_8.addWidget(self.rowHighlightChecker)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem4)
        self.snapPatternRepeatChecker = QtGui.QCheckBox(self.tab_2)
        self.snapPatternRepeatChecker.setChecked(True)
        self.snapPatternRepeatChecker.setObjectName(_fromUtf8("snapPatternRepeatChecker"))
        self.verticalLayout_8.addWidget(self.snapPatternRepeatChecker)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.customSymbolPathEdit = QtGui.QLineEdit(self.tab)
        self.customSymbolPathEdit.setObjectName(_fromUtf8("customSymbolPathEdit"))
        self.horizontalLayout_2.addWidget(self.customSymbolPathEdit)
        self.customSymbolPathButton = QtGui.QPushButton(self.tab)
        self.customSymbolPathButton.setAutoDefault(False)
        self.customSymbolPathButton.setObjectName(_fromUtf8("customSymbolPathButton"))
        self.horizontalLayout_2.addWidget(self.customSymbolPathButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(20, 80, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem6)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_6.addWidget(self.line)
        self.enableLoggingChecker = QtGui.QCheckBox(self.tab)
        self.enableLoggingChecker.setObjectName(_fromUtf8("enableLoggingChecker"))
        self.verticalLayout_6.addWidget(self.enableLoggingChecker)
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_6.addWidget(self.label_14)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.loggingPathEdit = QtGui.QLineEdit(self.tab)
        self.loggingPathEdit.setObjectName(_fromUtf8("loggingPathEdit"))
        self.horizontalLayout_9.addWidget(self.loggingPathEdit)
        self.loggingPathButton = QtGui.QPushButton(self.tab)
        self.loggingPathButton.setAutoDefault(False)
        self.loggingPathButton.setObjectName(_fromUtf8("loggingPathButton"))
        self.horizontalLayout_9.addWidget(self.loggingPathButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem7 = QtGui.QSpacerItem(20, 185, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_10.addWidget(self.tabWidget)
        spacerItem8 = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.makeDefaultButton = QtGui.QPushButton(PreferencesDialog)
        self.makeDefaultButton.setAutoDefault(False)
        self.makeDefaultButton.setObjectName(_fromUtf8("makeDefaultButton"))
        self.horizontalLayout.addWidget(self.makeDefaultButton)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.pushButton = QtGui.QPushButton(PreferencesDialog)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.label_7.setBuddy(self.highlightRowOpacitySpinner)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PreferencesDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "sconcho: Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Legend Font", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesDialog", "Family", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferencesDialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PreferencesDialog", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.legendTab), QtGui.QApplication.translate("PreferencesDialog", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Label Font", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("PreferencesDialog", "Family", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("PreferencesDialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("PreferencesDialog", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.showRowLabelChecker.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Show Row Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.customRowLabelsChecker.setText(QtGui.QApplication.translate("PreferencesDialog", "Use custom row labels (disables all automatic updates)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("PreferencesDialog", "even row label location", None, QtGui.QApplication.UnicodeUTF8))
        self.evenRowLabelLocationComboBox.setItemText(0, QtGui.QApplication.translate("PreferencesDialog", "right of chart", None, QtGui.QApplication.UnicodeUTF8))
        self.evenRowLabelLocationComboBox.setItemText(1, QtGui.QApplication.translate("PreferencesDialog", "left of chart", None, QtGui.QApplication.UnicodeUTF8))
        self.showRowsWithIntervalButton.setText(QtGui.QApplication.translate("PreferencesDialog", "show only every ", None, QtGui.QApplication.UnicodeUTF8))
        self.showOddRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "show only odd row labels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("PreferencesDialog", "odd row label location", None, QtGui.QApplication.UnicodeUTF8))
        self.oddRowLabelLocationComboBox.setItemText(0, QtGui.QApplication.translate("PreferencesDialog", "right of chart", None, QtGui.QApplication.UnicodeUTF8))
        self.oddRowLabelLocationComboBox.setItemText(1, QtGui.QApplication.translate("PreferencesDialog", "left of chart", None, QtGui.QApplication.UnicodeUTF8))
        self.showEvenRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "show only even row labels", None, QtGui.QApplication.UnicodeUTF8))
        self.rowLabelsStartLabel.setText(QtGui.QApplication.translate("PreferencesDialog", "label starting at row", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAllRowsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "show all  row labels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PreferencesDialog", "row labels start with", None, QtGui.QApplication.UnicodeUTF8))
        self.showColumnLabelChecker.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Show Column Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.customColumnLabelsChecker.setText(QtGui.QApplication.translate("PreferencesDialog", "Use custom column labels (disables all automatic updates)", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAllColumnsButton.setText(QtGui.QApplication.translate("PreferencesDialog", "label all columns", None, QtGui.QApplication.UnicodeUTF8))
        self.showColumnsWithIntervalButton.setText(QtGui.QApplication.translate("PreferencesDialog", "show only every ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("PreferencesDialog", "label starting at column", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.labelTab), QtGui.QApplication.translate("PreferencesDialog", "Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreferencesDialog", "Grid Cell Width (pixels)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PreferencesDialog", "Grid Cell Height (pixels)", None, QtGui.QApplication.UnicodeUTF8))
        self.rowHighlightChecker.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Highlight Grid Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PreferencesDialog", "&Opacity (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.highlightRowColorButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Highlight Color", None, QtGui.QApplication.UnicodeUTF8))
        self.highlightRowStartComboBox.setItemText(0, QtGui.QApplication.translate("PreferencesDialog", "start at bottom row", None, QtGui.QApplication.UnicodeUTF8))
        self.highlightRowStartComboBox.setItemText(1, QtGui.QApplication.translate("PreferencesDialog", "start at second row", None, QtGui.QApplication.UnicodeUTF8))
        self.snapPatternRepeatChecker.setText(QtGui.QApplication.translate("PreferencesDialog", "snap pattern repeats to grid", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("PreferencesDialog", "Grid Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PreferencesDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu LGC Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">Path to Custom Knitting Symbols Folder</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.customSymbolPathButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.enableLoggingChecker.setToolTip(QtGui.QApplication.translate("PreferencesDialog", "Enable logging of internal sconcho warnings/errors to file at logging Path. *Note* This setting requires a sconcho restart to take effect.", None, QtGui.QApplication.UnicodeUTF8))
        self.enableLoggingChecker.setText(QtGui.QApplication.translate("PreferencesDialog", "Enable logging", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("PreferencesDialog", "Logging Path", None, QtGui.QApplication.UnicodeUTF8))
        self.loggingPathButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PreferencesDialog", "Custom Symbols && Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.makeDefaultButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Make &Default", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PreferencesDialog", "&Close", None, QtGui.QApplication.UnicodeUTF8))

