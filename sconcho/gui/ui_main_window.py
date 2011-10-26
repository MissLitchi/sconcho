# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created: Tue Oct 25 22:24:50 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1048, 712)
        MainWindow.setWindowTitle(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sconcho_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.infoLayout = QtGui.QHBoxLayout()
        self.infoLayout.setObjectName(_fromUtf8("infoLayout"))
        self.activeSymbolWidget = ActiveSymbolWidget(self.centralwidget)
        self.activeSymbolWidget.setObjectName(_fromUtf8("activeSymbolWidget"))
        self.infoLayout.addWidget(self.activeSymbolWidget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.infoLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.infoLayout)
        self.graphicsView = PatternView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 742, 71))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.colorWidget = ColorWidget(self.scrollAreaWidgetContents)
        self.colorWidget.setObjectName(_fromUtf8("colorWidget"))
        self.verticalLayout_4.addWidget(self.colorWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menu_Zoom = QtGui.QMenu(self.menuView)
        self.menu_Zoom.setTitle(QtGui.QApplication.translate("MainWindow", "&Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Zoom.setObjectName(_fromUtf8("menu_Zoom"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuGrid = QtGui.QMenu(self.menubar)
        self.menuGrid.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGrid.setObjectName(_fromUtf8("menuGrid"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.symbolDockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.symbolDockWidget.sizePolicy().hasHeightForWidth())
        self.symbolDockWidget.setSizePolicy(sizePolicy)
        self.symbolDockWidget.setMinimumSize(QtCore.QSize(278, 212))
        self.symbolDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.symbolDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.symbolDockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "sconcho: available knitting symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.symbolDockWidget.setObjectName(_fromUtf8("symbolDockWidget"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.symbolCategoryChooser = QtGui.QComboBox(self.dockWidgetContents_3)
        self.symbolCategoryChooser.setObjectName(_fromUtf8("symbolCategoryChooser"))
        self.verticalLayout_3.addWidget(self.symbolCategoryChooser)
        self.symbolSelectorLayout = QtGui.QVBoxLayout()
        self.symbolSelectorLayout.setObjectName(_fromUtf8("symbolSelectorLayout"))
        self.verticalLayout_3.addLayout(self.symbolSelectorLayout)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 130))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Most Frequently Used Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea_2 = QtGui.QScrollArea(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 232, 86))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.recentlyUsedSymbolWidget = RecentlyUsedSymbolWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentlyUsedSymbolWidget.sizePolicy().hasHeightForWidth())
        self.recentlyUsedSymbolWidget.setSizePolicy(sizePolicy)
        self.recentlyUsedSymbolWidget.setObjectName(_fromUtf8("recentlyUsedSymbolWidget"))
        self.horizontalLayout_2.addWidget(self.recentlyUsedSymbolWidget)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.symbolDockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.symbolDockWidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionAbout_sconcho = QtGui.QAction(MainWindow)
        self.actionAbout_sconcho.setIcon(icon)
        self.actionAbout_sconcho.setText(QtGui.QApplication.translate("MainWindow", "About sconcho", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_sconcho.setObjectName(_fromUtf8("actionAbout_sconcho"))
        self.actionAbout_Qt4 = QtGui.QAction(MainWindow)
        self.actionAbout_Qt4.setText(QtGui.QApplication.translate("MainWindow", "About Qt4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt4.setObjectName(_fromUtf8("actionAbout_Qt4"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "&New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QtGui.QApplication.translate("MainWindow", "Start New Chart", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start New Chart", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/fileopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setToolTip(QtGui.QApplication.translate("MainWindow", "Open saved project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open saved project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setIcon(icon3)
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save  &as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setToolTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save project as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionExport = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/fileexport.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon4)
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "&Export Bitmap...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setToolTip(QtGui.QApplication.translate("MainWindow", "Export as image file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setStatusTip(QtGui.QApplication.translate("MainWindow", "Export as image file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon5)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("MainWindow", "Quit sconcho", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Quit sconcho", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionPrint = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/fileprint.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon6)
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "&Print...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setStatusTip(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionShow_pattern_grid = QtGui.QAction(MainWindow)
        self.actionShow_pattern_grid.setCheckable(True)
        self.actionShow_pattern_grid.setChecked(True)
        self.actionShow_pattern_grid.setText(QtGui.QApplication.translate("MainWindow", "Show &Pattern Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_pattern_grid.setToolTip(QtGui.QApplication.translate("MainWindow", "toggle visibility of pattern grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_pattern_grid.setStatusTip(QtGui.QApplication.translate("MainWindow", "toggle visibility of pattern ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_pattern_grid.setObjectName(_fromUtf8("actionShow_pattern_grid"))
        self.actionShow_legend = QtGui.QAction(MainWindow)
        self.actionShow_legend.setCheckable(True)
        self.actionShow_legend.setChecked(True)
        self.actionShow_legend.setText(QtGui.QApplication.translate("MainWindow", "Show &Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_legend.setToolTip(QtGui.QApplication.translate("MainWindow", "toggle visibility of legend", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_legend.setStatusTip(QtGui.QApplication.translate("MainWindow", "toggle visibility of legend", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_legend.setObjectName(_fromUtf8("actionShow_legend"))
        self.actionShow_grid_labels = QtGui.QAction(MainWindow)
        self.actionShow_grid_labels.setCheckable(True)
        self.actionShow_grid_labels.setChecked(True)
        self.actionShow_grid_labels.setText(QtGui.QApplication.translate("MainWindow", "Show &Grid Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_grid_labels.setToolTip(QtGui.QApplication.translate("MainWindow", "toggle visbility of grid labels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_grid_labels.setStatusTip(QtGui.QApplication.translate("MainWindow", "toggle visbility of grid labels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_grid_labels.setObjectName(_fromUtf8("actionShow_grid_labels"))
        self.action_Insert_delete_rows_and_columns = QtGui.QAction(MainWindow)
        self.action_Insert_delete_rows_and_columns.setText(QtGui.QApplication.translate("MainWindow", "&Insert/Delete Rows and Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Insert_delete_rows_and_columns.setStatusTip(QtGui.QApplication.translate("MainWindow", "insert/delete rows and columns", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Insert_delete_rows_and_columns.setObjectName(_fromUtf8("action_Insert_delete_rows_and_columns"))
        self.actionZoom_In = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-in.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon7)
        self.actionZoom_In.setText(QtGui.QApplication.translate("MainWindow", "Zoom &In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-out.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon8)
        self.actionZoom_Out.setText(QtGui.QApplication.translate("MainWindow", "Zoom &Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionFit = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-best-fit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFit.setIcon(icon9)
        self.actionFit.setText(QtGui.QApplication.translate("MainWindow", "&Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFit.setObjectName(_fromUtf8("actionFit"))
        self.actionSconcho_Manual = QtGui.QAction(MainWindow)
        self.actionSconcho_Manual.setIcon(icon)
        self.actionSconcho_Manual.setText(QtGui.QApplication.translate("MainWindow", "Sconcho Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSconcho_Manual.setObjectName(_fromUtf8("actionSconcho_Manual"))
        self.actionPrefs = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gtk-preferences.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrefs.setIcon(icon10)
        self.actionPrefs.setText(QtGui.QApplication.translate("MainWindow", "P&references", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrefs.setObjectName(_fromUtf8("actionPrefs"))
        self.action_Insert_delete_rows_and_columns1 = QtGui.QAction(MainWindow)
        self.action_Insert_delete_rows_and_columns1.setText(QtGui.QApplication.translate("MainWindow", "&Manage Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Insert_delete_rows_and_columns1.setObjectName(_fromUtf8("action_Insert_delete_rows_and_columns1"))
        self.action_Manage_Knitting_Symbols = QtGui.QAction(MainWindow)
        self.action_Manage_Knitting_Symbols.setText(QtGui.QApplication.translate("MainWindow", "&Manage Custom Knitting Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Manage_Knitting_Symbols.setObjectName(_fromUtf8("action_Manage_Knitting_Symbols"))
        self.actionUnselect_All = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gtk-clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnselect_All.setIcon(icon11)
        self.actionUnselect_All.setText(QtGui.QApplication.translate("MainWindow", "&Deselect All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnselect_All.setToolTip(QtGui.QApplication.translate("MainWindow", "Deselect all currently highlighted cells on the grid.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnselect_All.setObjectName(_fromUtf8("actionUnselect_All"))
        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setText(QtGui.QApplication.translate("MainWindow", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Copy.setObjectName(_fromUtf8("action_Copy"))
        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setObjectName(_fromUtf8("action_Paste"))
        self.actionCheck_Pattern_Grid = QtGui.QAction(MainWindow)
        self.actionCheck_Pattern_Grid.setText(QtGui.QApplication.translate("MainWindow", "Check Pattern Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_Pattern_Grid.setToolTip(QtGui.QApplication.translate("MainWindow", "Chech Pattern Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_Pattern_Grid.setObjectName(_fromUtf8("actionCheck_Pattern_Grid"))
        self.action_Normal = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/zoom-original.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Normal.setIcon(icon12)
        self.action_Normal.setText(QtGui.QApplication.translate("MainWindow", "&Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Normal.setObjectName(_fromUtf8("action_Normal"))
        self.action_Undo = QtGui.QAction(MainWindow)
        self.action_Undo.setText(QtGui.QApplication.translate("MainWindow", "&Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Undo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Undo.setObjectName(_fromUtf8("action_Undo"))
        self.action_Redo = QtGui.QAction(MainWindow)
        self.action_Redo.setText(QtGui.QApplication.translate("MainWindow", "&Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Redo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Redo.setObjectName(_fromUtf8("action_Redo"))
        self.actionShow_nostitch_symbols = QtGui.QAction(MainWindow)
        self.actionShow_nostitch_symbols.setCheckable(True)
        self.actionShow_nostitch_symbols.setChecked(True)
        self.actionShow_nostitch_symbols.setText(QtGui.QApplication.translate("MainWindow", "Show &Nostitch Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_nostitch_symbols.setObjectName(_fromUtf8("actionShow_nostitch_symbols"))
        self.actionCreate_Pattern_Repeat = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pattern_repeat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Pattern_Repeat.setIcon(icon13)
        self.actionCreate_Pattern_Repeat.setText(QtGui.QApplication.translate("MainWindow", "Create Pattern Repeat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Pattern_Repeat.setToolTip(QtGui.QApplication.translate("MainWindow", "Create a pattern repeat box around the currently highlighted cells.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Pattern_Repeat.setObjectName(_fromUtf8("actionCreate_Pattern_Repeat"))
        self.actionApply_Color_to_Selection = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/red_rect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionApply_Color_to_Selection.setIcon(icon14)
        self.actionApply_Color_to_Selection.setText(QtGui.QApplication.translate("MainWindow", "Apply Color to Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionApply_Color_to_Selection.setToolTip(QtGui.QApplication.translate("MainWindow", "Apply Color to Selection. Applies the currently selected color to all highlighted cells on the canvas.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionApply_Color_to_Selection.setObjectName(_fromUtf8("actionApply_Color_to_Selection"))
        self.actionCheck_for_updates = QtGui.QAction(MainWindow)
        self.actionCheck_for_updates.setText(QtGui.QApplication.translate("MainWindow", "Check for updates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_for_updates.setObjectName(_fromUtf8("actionCheck_for_updates"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menu_Zoom.addAction(self.actionZoom_In)
        self.menu_Zoom.addAction(self.actionZoom_Out)
        self.menu_Zoom.addAction(self.actionFit)
        self.menu_Zoom.addAction(self.action_Normal)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menu_Zoom.menuAction())
        self.menuView.addAction(self.action_Insert_delete_rows_and_columns)
        self.menuView.addAction(self.actionUnselect_All)
        self.menuView.addAction(self.actionCreate_Pattern_Repeat)
        self.menuView.addAction(self.actionApply_Color_to_Selection)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_pattern_grid)
        self.menuView.addAction(self.actionShow_grid_labels)
        self.menuView.addAction(self.actionShow_legend)
        self.menuHelp.addAction(self.actionSconcho_Manual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addAction(self.actionAbout_sconcho)
        self.menuHelp.addAction(self.actionAbout_Qt4)
        self.menuGrid.addSeparator()
        self.menuGrid.addAction(self.action_Undo)
        self.menuGrid.addAction(self.action_Redo)
        self.menuGrid.addSeparator()
        self.menuGrid.addAction(self.action_Manage_Knitting_Symbols)
        self.menuGrid.addSeparator()
        self.menuGrid.addAction(self.actionPrefs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGrid.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addAction(self.actionFit)
        self.toolBar.addAction(self.action_Normal)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUnselect_All)
        self.toolBar.addAction(self.actionCreate_Pattern_Repeat)
        self.toolBar_2.addAction(self.actionApply_Color_to_Selection)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

from active_symbol_widget import ActiveSymbolWidget
from color_widget import ColorWidget
from pattern_view import PatternView
from recently_used_symbol_widget import RecentlyUsedSymbolWidget
import icons_rc
