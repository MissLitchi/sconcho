# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/preferencesDialog.ui'
#
# Created: Sat Dec 18 16:01:20 2010
#      by: PyQt4 UI code generator 4.8.1
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
        PreferencesDialog.resize(392, 459)
        self.verticalLayout_3 = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
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
        self.tabWidget.addTab(self.legendTab, _fromUtf8(""))
        self.labelTab = QtGui.QWidget()
        self.labelTab.setObjectName(_fromUtf8("labelTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.labelTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
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
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.labelTab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.labelIntervalSpinner = QtGui.QSpinBox(self.groupBox_3)
        self.labelIntervalSpinner.setMinimum(1)
        self.labelIntervalSpinner.setMaximum(10)
        self.labelIntervalSpinner.setObjectName(_fromUtf8("labelIntervalSpinner"))
        self.horizontalLayout_3.addWidget(self.labelIntervalSpinner)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.labelTab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        spacerItem1 = QtGui.QSpacerItem(20, 236, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(PreferencesDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

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
        self.groupBox_3.setTitle(QtGui.QApplication.translate("PreferencesDialog", "Label Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("PreferencesDialog", "Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.labelTab), QtGui.QApplication.translate("PreferencesDialog", "Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("PreferencesDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

