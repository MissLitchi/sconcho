# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/insertDeleteRowColumnWidget.ui'
#
# Created: Sat Oct 30 11:48:19 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_InsertDeleteRowColumnWidget(object):
    def setupUi(self, InsertDeleteRowColumnWidget):
        InsertDeleteRowColumnWidget.setObjectName(_fromUtf8("InsertDeleteRowColumnWidget"))
        InsertDeleteRowColumnWidget.resize(636, 157)
        self.verticalLayout_2 = QtGui.QVBoxLayout(InsertDeleteRowColumnWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(InsertDeleteRowColumnWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.numInsertRows = QtGui.QSpinBox(self.tab)
        self.numInsertRows.setMinimum(1)
        self.numInsertRows.setMaximum(1000)
        self.numInsertRows.setObjectName(_fromUtf8("numInsertRows"))
        self.horizontalLayout.addWidget(self.numInsertRows)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.insertRowMode = QtGui.QComboBox(self.tab)
        self.insertRowMode.setObjectName(_fromUtf8("insertRowMode"))
        self.insertRowMode.addItem(_fromUtf8(""))
        self.insertRowMode.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.insertRowMode)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.insertRowPivot = QtGui.QSpinBox(self.tab)
        self.insertRowPivot.setMinimum(1)
        self.insertRowPivot.setMaximum(1000)
        self.insertRowPivot.setObjectName(_fromUtf8("insertRowPivot"))
        self.horizontalLayout.addWidget(self.insertRowPivot)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.insertRowButton = QtGui.QPushButton(self.tab)
        self.insertRowButton.setObjectName(_fromUtf8("insertRowButton"))
        self.horizontalLayout.addWidget(self.insertRowButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.deleteRowID = QtGui.QSpinBox(self.tab_2)
        self.deleteRowID.setMinimum(1)
        self.deleteRowID.setMaximum(1000)
        self.deleteRowID.setObjectName(_fromUtf8("deleteRowID"))
        self.horizontalLayout_5.addWidget(self.deleteRowID)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.deleteRowButton = QtGui.QPushButton(self.tab_2)
        self.deleteRowButton.setObjectName(_fromUtf8("deleteRowButton"))
        self.horizontalLayout_5.addWidget(self.deleteRowButton)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.numInsertColumns = QtGui.QSpinBox(self.tab_3)
        self.numInsertColumns.setMinimum(1)
        self.numInsertColumns.setMaximum(1000)
        self.numInsertColumns.setObjectName(_fromUtf8("numInsertColumns"))
        self.horizontalLayout_3.addWidget(self.numInsertColumns)
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.insertColumnMode = QtGui.QComboBox(self.tab_3)
        self.insertColumnMode.setObjectName(_fromUtf8("insertColumnMode"))
        self.insertColumnMode.addItem(_fromUtf8(""))
        self.insertColumnMode.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.insertColumnMode)
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.insertColumnPivot = QtGui.QSpinBox(self.tab_3)
        self.insertColumnPivot.setMinimum(1)
        self.insertColumnPivot.setMaximum(1000)
        self.insertColumnPivot.setObjectName(_fromUtf8("insertColumnPivot"))
        self.horizontalLayout_3.addWidget(self.insertColumnPivot)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.insertColumnButton = QtGui.QPushButton(self.tab_3)
        self.insertColumnButton.setObjectName(_fromUtf8("insertColumnButton"))
        self.horizontalLayout_3.addWidget(self.insertColumnButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.deleteColumnID = QtGui.QSpinBox(self.tab_4)
        self.deleteColumnID.setMinimum(1)
        self.deleteColumnID.setMaximum(1000)
        self.deleteColumnID.setObjectName(_fromUtf8("deleteColumnID"))
        self.horizontalLayout_6.addWidget(self.deleteColumnID)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.deleteColumnButton = QtGui.QPushButton(self.tab_4)
        self.deleteColumnButton.setObjectName(_fromUtf8("deleteColumnButton"))
        self.horizontalLayout_6.addWidget(self.deleteColumnButton)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.closeButton = QtGui.QPushButton(InsertDeleteRowColumnWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_9.addWidget(self.closeButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(InsertDeleteRowColumnWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InsertDeleteRowColumnWidget)

    def retranslateUi(self, InsertDeleteRowColumnWidget):
        InsertDeleteRowColumnWidget.setWindowTitle(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert/delete rows and columns", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "rows", None, QtGui.QApplication.UnicodeUTF8))
        self.insertRowMode.setItemText(0, QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "below", None, QtGui.QApplication.UnicodeUTF8))
        self.insertRowMode.setItemText(1, QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "above", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "row", None, QtGui.QApplication.UnicodeUTF8))
        self.insertRowButton.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert row", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "delete row", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteRowButton.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "delete row", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "columns", None, QtGui.QApplication.UnicodeUTF8))
        self.insertColumnMode.setItemText(0, QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "left of", None, QtGui.QApplication.UnicodeUTF8))
        self.insertColumnMode.setItemText(1, QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "right of", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "column", None, QtGui.QApplication.UnicodeUTF8))
        self.insertColumnButton.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "insert column", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "delete column", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteColumnButton.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "delete column", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("InsertDeleteRowColumnWidget", "Close", None, QtGui.QApplication.UnicodeUTF8))

