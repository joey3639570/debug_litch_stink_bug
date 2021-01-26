# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '20200727_demo.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from datetime import datetime
import json
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        # Tab1 -  detection demo
        self.centralwidget = QtWidgets.QWidget(MainWindow) # parent is MainWindow
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget) # parent is centralWidget
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget() # declaration for tab, no inheritance needed
        self.tab1.setObjectName("tab1")

        # Instructions for selecting orchard
        self.tab1_orchard_instruction_label = QtWidgets.QLabel(self.tab1)
        self.tab1_orchard_instruction_label.setObjectName("tab1_orchard_instruction_label")
        self.tab1_orchard_instruction_label_font = QtGui.QFont()
        self.tab1_orchard_instruction_label_font.setPointSize(12)
        self.tab1_orchard_instruction_label.setFont(self.tab1_orchard_instruction_label_font)

        # ComboBox for selecting orchard
        self.tab1_orchard_comboBox = QtWidgets.QComboBox(self.tab1)
        self.tab1_orchard_comboBox.setObjectName('tab1_orchard_comboBox')
        self.tab1_orchard_comboBox.addItem('Orchard 1')
        self.tab1_orchard_comboBox.addItem('Orchard 2')
        self.tab1_orchard_comboBox.addItem('Orchard 3')
        
        # Instructions for selecting picture
        self.tab1_picture_instruction_label = QtWidgets.QLabel(self.tab1)
        self.tab1_picture_instruction_label.setObjectName("tab1_picture_instruction_label")
        self.tab1_picture_instruction_label_font = QtGui.QFont()
        self.tab1_picture_instruction_label_font.setPointSize(12)
        self.tab1_picture_instruction_label.setFont(self.tab1_picture_instruction_label_font)
        
        # Button for selecting picture
        self.tab1_picture_button = QtWidgets.QPushButton(self.tab1)  # parent is tab, which declares at line 26
        self.tab1_picture_button.setFixedWidth(140)
        self.tab1_picture_button.setMouseTracking(True)
        self.tab1_picture_button.setObjectName("tab1_picture_button")

        # Text for showing the path of the pic
        self.tab1_picture_path_lineEdit = QtWidgets.QLineEdit(self.tab1) # parent is tab
        self.tab1_picture_path_lineEdit.setObjectName("tab1_picture_path_lineEdit")
        self.tab1_picture_path = ''
        
        # Running state
        self.tab1_state_label = QtWidgets.QLabel(self.tab1)
        self.tab1_state_label.setObjectName("tab1_state_label")

        # Button for performing the test
        self.tab1_test_button = QtWidgets.QPushButton(self.tab1)  # parent is tab
        self.tab1_test_button.setMouseTracking(True)
        self.tab1_test_button.setObjectName("tab1_test_button")

        # Seperate line for buttons and pictures
        self.tab1_line = QtWidgets.QFrame(self.tab1) # parent is tab
        self.tab1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab1_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab1_line.setObjectName("tab1_line")

        # Label for showing statistical data
        self.tab1_statistical_data_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_label.setFixedHeight(64)
        self.tab1_statistical_data_label.setObjectName("tab1_statistical_data_label")

        # Left grid for original picture
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Button, brush)

        self.tab1_left_picture = QtWidgets.QLabel(self.tab1)
        self.tab1_left_picture.setObjectName("tab1_left_picture")
        self.tab1_left_picture.setFixedHeight(416)
        self.tab1_left_picture.setFixedWidth(560)
        self.tab1_left_picture_navigate_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_left_picture_navigate_button.setEnabled(False)
        self.tab1_left_picture_navigate_button.setMouseTracking(True)
        self.tab1_left_picture_navigate_button.setFixedWidth(51)
        self.tab1_left_picture_navigate_button.setFixedHeight(416)
        self.tab1_left_picture_navigate_button.setObjectName("tab1_left_picture_navigate_button")
        self.tab1_left_picture_navigate_button.setPalette(palette)
        
        # Right grid for detected picture
        self.tab1_right_picture = QtWidgets.QLabel(self.tab1)
        self.tab1_right_picture.setObjectName("tab1_right_picture")
        self.tab1_right_picture.setFixedHeight(416)
        self.tab1_right_picture.setFixedWidth(560)
        self.tab1_right_picture_navigate_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_right_picture_navigate_button.setEnabled(False)
        self.tab1_right_picture_navigate_button.setMouseTracking(True)
        self.tab1_right_picture_navigate_button.setFixedWidth(51)
        self.tab1_right_picture_navigate_button.setFixedHeight(416)
        self.tab1_right_picture_navigate_button.setObjectName("tab1_right_picture_navigate_button")
        self.tab1_right_picture_navigate_button.setPalette(palette)

        self.tab1_picture_navigate_button_font = QtGui.QFont()
        self.tab1_picture_navigate_button_font.setPointSize(14)
        self.tab1_left_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)
        self.tab1_right_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)

        # Nesting layout
        self.tab1_verticalLayout = QtWidgets.QVBoxLayout(self.tab1)  # parent is tab. In order to line up widgets under self.tab1???
        self.tab1_orchard_widget = QtWidgets.QWidget()
        self.tab1_orchard_widget_layout = QtWidgets.QVBoxLayout(self.tab1_orchard_widget)
        self.tab1_picture_selection_widget = QtWidgets.QWidget()
        self.tab1_picture_selection_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_selection_widget)
        self.tab1_test_widget = QtWidgets.QWidget()
        self.tab1_test_widget_layout = QtWidgets.QVBoxLayout(self.tab1_test_widget)  # parent is tab. In order to line up widgets under tab1_test_widget???
        self.tab1_statistical_data_widget = QtWidgets.QWidget()
        self.tab1_statistical_data_widget_layout = QtWidgets.QHBoxLayout(self.tab1_statistical_data_widget)
        self.tab1_picture_widget = QtWidgets.QWidget()
        self.tab1_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_widget) # parent is tab. In order to line up widgets under tab1_picture_widget???

        # orchard widget
        self.tab1_orchard_widget_layout.addWidget(self.tab1_orchard_comboBox)

        # picture path widget
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_button)
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_path_lineEdit)

        # detection widget
        self.tab1_test_widget_layout.addWidget(self.tab1_test_button)

        # statistical data widget
        self.tab1_statistical_data_widget_layout.addWidget(self.tab1_statistical_data_label)

        # pichture showing widget
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture_navigate_button)
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture_navigate_button)
        self.tab1_picture_widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # whole layout
        self.tab1_verticalLayout.addWidget(self.tab1_orchard_instruction_label)
        self.tab1_verticalLayout.addWidget(self.tab1_orchard_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_instruction_label)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_selection_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_test_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_line)
        self.tab1_verticalLayout.addWidget(self.tab1_statistical_data_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_state_label)
        self.tab1_verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        
        # Add tab1 and things above into the tabWidget
        self.tabWidget.addTab(self.tab1, "")
        

        # Tab2 - statistical data
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        
        # Instruction for selecting orchard
        self.tab2_orchard_instruction_label = QtWidgets.QLabel(self.tab2)
        self.tab2_orchard_instruction_label.setObjectName("tab2_orchard_instruction_label")
        self.tab2_orchard_instruction_label_font = QtGui.QFont()
        self.tab2_orchard_instruction_label_font.setPointSize(12)
        self.tab2_orchard_instruction_label.setFont(self.tab2_orchard_instruction_label_font)

        # ComboBox for selecting orchard
        self.tab2_orchard_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_orchard_comboBox.setObjectName('tab2_orchard_comboBox')
        self.tab2_orchard_comboBox.addItem('Orchard 1')
        self.tab2_orchard_comboBox.addItem('Orchard 2')
        self.tab2_orchard_comboBox.addItem('Orchard 3')

        # Running state
        self.tab2_state_label = QtWidgets.QLabel(self.tab2)
        self.tab2_state_label.setObjectName('tab2_state_label')

        # Instruction for selecting date
        self.tab2_date_instruction_label = QtWidgets.QLabel(self.tab2)
        self.tab2_date_instruction_label.setObjectName("tab2_date_instruction_label")
        self.tab2_date_instruction_label_font = QtGui.QFont()
        self.tab2_date_instruction_label_font.setPointSize(12)
        self.tab2_date_instruction_label.setFont(self.tab2_date_instruction_label_font)

        # Date selection
        self.tab2_date_label = QtWidgets.QLabel(self.tab2)
        self.tab2_date_label.setObjectName('tab2_date_label')
        self.tab2_date_label.setAlignment(QtCore.Qt.AlignCenter)

        self.tab2_date_font = QtGui.QFont()
        self.tab2_date_font.setPointSize(12)
        self.tab2_date_label.setFont(self.tab2_date_font)

        self.tab2_left_date_navigate_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_left_date_navigate_button.setFixedWidth(140)
        self.tab2_left_date_navigate_button.setEnabled(False)
        self.tab2_left_date_navigate_button.setMouseTracking(True)
        self.tab2_left_date_navigate_button.setObjectName("tab2_left_date_navigate_button")
        self.tab2_left_date_navigate_button.setFont(self.tab2_date_font)

        self.tab2_right_date_navigate_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_right_date_navigate_button.setFixedWidth(140)
        self.tab2_right_date_navigate_button.setEnabled(False)
        self.tab2_right_date_navigate_button.setMouseTracking(True)
        self.tab2_right_date_navigate_button.setObjectName("tab2_right_date_navigate_button")
        self.tab2_right_date_navigate_button.setFont(self.tab2_date_font)
        
        # Line that seperates date selection buttons and statistical data
        self.tab2_line = QtWidgets.QFrame(self.tab2) # parent is tab
        self.tab2_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab2_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab2_line.setObjectName("tab2_line")

        # Label for showing statistical data
        self.tab2_statistical_data_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_label.setFixedHeight(64)
        self.tab2_statistical_data_label.setObjectName('tab2_statistical_data_label')

        # Left grid for original picture
        self.tab2_left_picture = QtWidgets.QLabel(self.tab2)
        self.tab2_left_picture.setObjectName("tab2_left_picture")
        self.tab2_left_picture.setFixedHeight(416)
        self.tab2_left_picture.setFixedWidth(560)
        self.tab2_left_picture_navigate_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_left_picture_navigate_button.setEnabled(False)
        self.tab2_left_picture_navigate_button.setMouseTracking(True)
        self.tab2_left_picture_navigate_button.setFixedWidth(51)
        self.tab2_left_picture_navigate_button.setFixedHeight(416)
        self.tab2_left_picture_navigate_button.setObjectName("tab2_left_picture_navigate_button")
        self.tab2_left_picture_navigate_button.setPalette(palette)
        
        # Right grid for detected picture
        self.tab2_right_picture = QtWidgets.QLabel(self.tab2)
        self.tab2_right_picture.setObjectName("tab2_right_picture")
        self.tab2_right_picture.setFixedHeight(416)
        self.tab2_right_picture.setFixedWidth(560)
        self.tab2_right_picture_navigate_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_right_picture_navigate_button.setEnabled(False)
        self.tab2_right_picture_navigate_button.setMouseTracking(True)
        self.tab2_right_picture_navigate_button.setFixedWidth(51)
        self.tab2_right_picture_navigate_button.setFixedHeight(416)
        self.tab2_right_picture_navigate_button.setObjectName("tab2_right_picture_navigate_button")
        self.tab2_right_picture_navigate_button.setPalette(palette)

        self.tab2_left_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)
        self.tab2_right_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)

        # nesting layout
        self.tab2_verticalLayout = QtWidgets.QVBoxLayout(self.tab2)  # parent is tab. In order to line up widgets under self.tab1???
        self.tab2_orchard_widget = QtWidgets.QWidget()
        self.tab2_orchard_widget_layout = QtWidgets.QVBoxLayout(self.tab2_orchard_widget)
        self.tab2_date_selection_widget = QtWidgets.QWidget()
        self.tab2_date_selection_widget_layout = QtWidgets.QHBoxLayout(self.tab2_date_selection_widget)
        self.tab2_statistical_data_widget = QtWidgets.QWidget()
        self.tab2_statistical_data_widget_layout = QtWidgets.QVBoxLayout(self.tab2_statistical_data_widget)
        self.tab2_picture_widget = QtWidgets.QWidget()
        self.tab2_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab2_picture_widget)

        # orchard comboBox and running state
        self.tab2_orchard_widget_layout.addWidget(self.tab2_orchard_comboBox)

        # date selection widget
        self.tab2_date_selection_widget_layout.addWidget(self.tab2_left_date_navigate_button)
        self.tab2_date_selection_widget_layout.addWidget(self.tab2_date_label)
        self.tab2_date_selection_widget_layout.addWidget(self.tab2_right_date_navigate_button)

        # pichture showing widget
        self.tab2_picture_widget_layout.addWidget(self.tab2_left_picture_navigate_button)
        self.tab2_picture_widget_layout.addWidget(self.tab2_left_picture)
        self.tab2_picture_widget_layout.addWidget(self.tab2_right_picture)
        self.tab2_picture_widget_layout.addWidget(self.tab2_right_picture_navigate_button)
        self.tab2_picture_widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.tab2_statistical_data_widget_layout.addWidget(self.tab2_statistical_data_label)

        # whole layout
        self.tab2_verticalLayout.addWidget(self.tab2_orchard_instruction_label)
        self.tab2_verticalLayout.addWidget(self.tab2_orchard_widget)
        self.tab2_verticalLayout.addWidget(self.tab2_date_instruction_label)
        self.tab2_verticalLayout.addWidget(self.tab2_date_selection_widget)
        self.tab2_verticalLayout.addWidget(self.tab2_line)
        self.tab2_verticalLayout.addWidget(self.tab2_statistical_data_widget)
        self.tab2_verticalLayout.addWidget(self.tab2_picture_widget)
        self.tab2_verticalLayout.addWidget(self.tab2_state_label)
        self.tab2_verticalLayout.setAlignment(QtCore.Qt.AlignTop)

        # Add tab2 and things above into the tabWidget
        self.tabWidget.addTab(self.tab2, "")

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tessaratoma Recognition"))

        # tab 1
        self.tab1_orchard_instruction_label.setText(_translate("MainWindow", "1. Select the orchard"))
        self.tab1_picture_instruction_label.setText(_translate("MainWindow", "2. Click \"Browse\" to select the directory containing the pictures to detect"))
        self.tab1_picture_button.setText(_translate("MainWindow", "Browse"))
        self.tab1_test_button.setText(_translate("MainWindow", "DETECT"))
        self.tab1_state_label.setText(_translate("MainWindow", "Ready"))
        self.tab1_left_picture_navigate_button.setText(_translate("MainWindow", "<"))
        self.tab1_right_picture_navigate_button.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Detection"))
        
        # tab 2
        self.tab2_orchard_instruction_label.setText(_translate("MainWindow", "1. Select the orchard"))
        self.tab2_state_label.setText(_translate("MainWindow", "Ready"))
        self.tab2_date_instruction_label.setText(_translate("MainWindow", "2. Select the date"))
        self.tab2_left_date_navigate_button.setText(_translate("MainWindow", "<"))
        self.tab2_right_date_navigate_button.setText(_translate("MainWindow", ">"))
        self.tab2_left_picture_navigate_button.setText(_translate("MainWindow", "<"))
        self.tab2_right_picture_navigate_button.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Statistical data"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QtWidgets.QMainWindow.__init__(self)

        # Initialize UI
        self.setupUi(self)

        # variables for showing pictures in tab1
        self.tab1_detectionOutputPath = ''
        self.tab1_originalPictureDirectoryPath = ''
        self.tab1_originalPictureAddresses = []
        self.tab1_pictureNavigateCount = 0

        # variables for showing statistical data
        self.tab2_detectionOutputPaths = []
        self.tab2_outputNavigateCount = 0
        
        self.tab2_originalPictureDirectoryPath = ''
        self.tab2_originalPictureAddresses = []
        self.tab2_pictureNavigateCount = 0

        # Signal Setting
        # tab bar
        self.tabWidget.currentChanged['int'].connect(self.on_tabWidget_changed)

        # tab1
        self.tab1_picture_button.clicked.connect(self.on_tab1_picture_button_clicked)
        self.tab1_test_button.clicked.connect(self.on_tab1_test_button_clicked)
        self.tab1_left_picture_navigate_button.clicked.connect(self.on_tab1_left_picutre_navigate_button_clicked)
        self.tab1_right_picture_navigate_button.clicked.connect(self.on_tab1_right_picutre_navigate_button_clicked)
        
        # tab2
        self.tab2_orchard_comboBox.currentIndexChanged.connect(self.on_tab2_comboBox_changed)
        self.tab2_left_picture_navigate_button.clicked.connect(self.on_tab2_left_picutre_navigate_button_clicked)
        self.tab2_right_picture_navigate_button.clicked.connect(self.on_tab2_right_picutre_navigate_button_clicked)
        self.tab2_left_date_navigate_button.clicked.connect(self.on_tab2_left_date_navigate_button_clicked)
        self.tab2_right_date_navigate_button.clicked.connect(self.on_tab2_right_date_navigate_button_clicked)

        # variables for line edit style
        self.lineEditOriginalStyle = self.tab1_picture_path_lineEdit.styleSheet()

    
    def tr(self, text):
        return QtCore.QObject.tr(self, text)


    def on_tabWidget_changed(self, index):
        if index == 0:
            self.tab1_state_label.setText(self.tr('Ready'))
        elif index == 1:
            self.tab2_statistical_data_label.clear()
            self.tab2_date_label.clear()
            self.tab2_left_picture.clear()
            self.tab2_right_picture.clear()
            self.tab2_orchard_comboBox.setEnabled(False)
            self.tab2_left_picture_navigate_button.setEnabled(False)
            self.tab2_right_picture_navigate_button.setEnabled(False)
            self.tab2_left_date_navigate_button.setEnabled(False)
            self.tab2_right_date_navigate_button.setEnabled(False)
            self.tab2_outputNavigateCount = 0
            self.tab2_detectionOutputPaths = []

            self.tab2_state_label.setText(self.tr('Loading. Please wait...'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            
            collect_output_paths_return = self.tab2_collect_output_paths()

            if collect_output_paths_return == 1 or collect_output_paths_return == 2:
                self.tab2_date_label.setText(self.tr('No data to show'))
                self.tab2_state_label.setText(self.tr('Ready'))
                QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
                return
            
            f = open(self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount] + 'statistics.json')
            openedStatisticalData = json.load(f)
            f.close()

            self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']
            
            self.tab2_update_statistical_data(openedStatisticalData)

            self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                                self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                                self.tab2_left_picture,
                                self.tab2_right_picture)

            self.tab2_orchard_comboBox.setEnabled(True)
            if len(self.tab2_detectionOutputPaths) > 1:
                self.tab2_right_date_navigate_button.setEnabled(True)
            
            if len(self.tab2_originalPictureAddresses) > 1:
                self.tab2_right_picture_navigate_button.setEnabled(True)
            
            self.tab2_state_label.setText(self.tr('Ready'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            
        return

    def update_pictures(self, leftPictureAddress, rightPictureAddress, left_picture, right_picture):
        left_pixmap = QtGui.QPixmap(leftPictureAddress)
        left_pixmap = left_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        left_picture.setPixmap(left_pixmap)
        right_pixmap = QtGui.QPixmap(rightPictureAddress)
        right_pixmap = right_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        right_picture.setPixmap(right_pixmap)

        return


    def on_tab1_picture_button_clicked(self):
        source = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr('Select directory'), '/home/mmnlab/')
        if source:
            self.tab1_picture_path_lineEdit.setText(source)
            self.tab1_picture_path = source + '/'
            self.tab1_picture_path_lineEdit.setStyleSheet(self.lineEditOriginalStyle)
            self.tab1_state_label.setText(self.tr('Selected directory: ' + source))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        elif source == '':
            if self.tab1_picture_path_lineEdit.text() == '':
                self.tab1_picture_path_lineEdit.setStyleSheet("border: 1px solid red;")
                self.tab1_state_label.setText(self.tr('No directory selected. Please select a directory to run the detection'))
                QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return


    def on_tab1_test_button_clicked(self):
        # protection
        if self.tab1_picture_path == '':
            self.tab1_picture_path_lineEdit.setStyleSheet("border: 1px solid red;")
            self.tab1_state_label.setText(self.tr('No directory selected. Please select a directory before running the detection'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            return

        # initialization
        self.tab1_orchard_comboBox.setEnabled(False)
        self.tab1_picture_button.setEnabled(False)
        self.tab1_picture_path_lineEdit.setEnabled(False)
        self.tab1_test_button.setEnabled(False)
        self.tab1_originalPictureDirectoryPath = self.tab1_picture_path
        self.tab1_pictureNavigateCount = 0
        self.tab1_originalPictureAddresses = []

        # create directory to store detected samples and detection log
        self.tab1_detectionOutputPath = os.path.abspath('.') + '/detection_output/'
        if os.path.isdir(self.tab1_detectionOutputPath) is False:
            os.mkdir(self.tab1_detectionOutputPath)
            self.tab1_state_label.setText(self.tr('Directory: ' + self.tab1_detectionOutputPath + ' created'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        else:
            self.tab1_state_label.setText(self.tr('Directory: ' + self.tab1_detectionOutputPath + ' already existed'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        resultDirectoryName = self.tab1_orchard_comboBox.currentText().replace(' ', '_') + '_' + date.replace('/', '').replace(':', '').replace(' ', '_')
        self.tab1_detectionOutputPath = self.tab1_detectionOutputPath + resultDirectoryName + '/'
        os.mkdir(self.tab1_detectionOutputPath)

        self.tab1_state_label.setText(self.tr('Directory: ' + self.tab1_detectionOutputPath + ' created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # create empty detection log file
        commands = ['touch',
                    self.tab1_detectionOutputPath + 'detection_results.json']
        os.system(' '.join(commands))

        self.tab1_state_label.setText(self.tr('Detection log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        # create empty statistics log file
        commands = ['touch',
                    self.tab1_detectionOutputPath + 'statistics.json']
        os.system(' '.join(commands))

        self.tab1_state_label.setText(self.tr('Statistics log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # run the detection
        ### batch images detector (darknet) provided by vincentgong7 ###
        self.tab1_state_label.setText(self.tr('Detection started, please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        commands = ['./darknet detector batch',
                    'data/obj.data',
                    'cfg/yolov4-custom.cfg',
                    'weights/20200509_20000iterations_random0_sub32_wh480/yolov4-custom_20000.weights',
                    'io_folder ' + self.tab1_originalPictureDirectoryPath,
                    self.tab1_detectionOutputPath,
                    '-out ' + self.tab1_detectionOutputPath + 'detection_results.json',
                    '-dont_show']
        os.system(' '.join(commands))
        
        self.tab1_state_label.setText(self.tr('Detection finished'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # collecting paths to all the pictures waiting to run the detection
        self.tab1_state_label.setText(self.tr('Collecting paths'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        for f in os.listdir(self.tab1_originalPictureDirectoryPath):
            if (f.lower().__contains__('.jpg')):
                self.tab1_originalPictureAddresses.append(self.tab1_originalPictureDirectoryPath + f)
            elif (f.lower().__contains__('.jpeg')):
                self.tab1_originalPictureAddresses.append(self.tab1_originalPictureDirectoryPath + f)
            elif (f.lower().__contains__('.png')):
                self.tab1_originalPictureAddresses.append(self.tab1_originalPictureDirectoryPath + f)
        
        self.tab1_originalPictureAddresses.sort()

        # statistical data
        self.tab1_state_label.setText(self.tr('Generating statistical data'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        detectedObjectCount = [0, 0, 0, 0, 0]

        f = open(self.tab1_detectionOutputPath + 'detection_results.json')
        openedResult = json.load(f)
        for r in openedResult:
            for o in r['objects']:
                if o['name'] == 'egg':
                    detectedObjectCount[0] = detectedObjectCount[0] + 1
                elif o['name'] == 'larval_before':
                    detectedObjectCount[1] = detectedObjectCount[1] + 1
                elif o['name'] == 'larval_after':
                    detectedObjectCount[2] = detectedObjectCount[2] + 1
                elif o['name'] == 'juvenile':
                    detectedObjectCount[3] = detectedObjectCount[3] + 1
                elif o['name'] == 'tessaratoma':
                    detectedObjectCount[4] = detectedObjectCount[4] + 1
        
        f.close()

        dominantObject = 0
        for i in range(1, len(detectedObjectCount)):
            if detectedObjectCount[dominantObject] < detectedObjectCount[i]:
                dominantObject = i
        
        if dominantObject == 0:
            dominantObject = 'egg'
        elif dominantObject == 1:
            dominantObject = 'larval_before'
        elif dominantObject == 2:
            dominantObject = 'larval_after'
        elif dominantObject == 3:
            dominantObject = 'juvenile'
        elif dominantObject == 4:
            dominantObject = 'tessaratoma'

        statisticsDictionary = {
            "time": date,
            "orchard": self.tab1_orchard_comboBox.currentText(), 
            "detection_result_path": self.tab1_detectionOutputPath + 'detection_results.json',
            "detected_directory": self.tab1_originalPictureDirectoryPath,
            "dominant_object": dominantObject,
            "objects_count": {"egg": detectedObjectCount[0], "larval_before": detectedObjectCount[1], "larval_after": detectedObjectCount[2], "juvenile": detectedObjectCount[3], "tessaratoma": detectedObjectCount[4]}
        }

        with open(self.tab1_detectionOutputPath + 'statistics.json', 'w') as outfile:
            outfile.write(json.dumps(statisticsDictionary, indent=4))
        
        self.tab1_state_label.setText(self.tr('Statistical data saved successfully'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        statisticalDataToShow = date + ' , at ' + statisticsDictionary['orchard'] + '\n' + \
                                 'DOMINANT OBJECT: ' + dominantObject.upper() + '\n' + \
                                 '    ' + 'egg: ' + str(detectedObjectCount[0]) + ' detected\n' + \
                                 '    ' + 'larval_before: ' + str(detectedObjectCount[1]) + ' detected\n' + \
                                 '    ' + 'larval_after: ' + str(detectedObjectCount[2]) + ' detected\n' + \
                                 '    ' + 'juvenile: ' + str(detectedObjectCount[3]) + ' detected\n' + \
                                 '    ' + 'tessaratoma: ' + str(detectedObjectCount[4]) + ' detected\n'

        # show pictures
        self.update_pictures(self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount],
                            self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount].replace(self.tab1_originalPictureDirectoryPath, self.tab1_detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab1_left_picture,
                            self.tab1_right_picture)

        # show statistical data in main window
        self.tab1_statistical_data_label.setText(self.tr(statisticalDataToShow.replace('    ', '').replace('detected\n', '    ')))

        # show statistical data in message box
        statisticalDataMessage = QtWidgets.QMessageBox()
        statisticalDataMessage.setWindowTitle(self.tr('Statistical result'))
        statisticalDataMessage.setInformativeText(self.tr(statisticalDataToShow))
        statisticalDataMessage.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        statisticalDataMessage.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
        statisticalDataMessage.exec()

        self.tab1_orchard_comboBox.setEnabled(True)
        self.tab1_picture_button.setEnabled(True)
        self.tab1_picture_path_lineEdit.setEnabled(True)
        self.tab1_test_button.setEnabled(True)
        if len(self.tab1_originalPictureAddresses) > 1:
            self.tab1_right_picture_navigate_button.setEnabled(True)

        self.tab1_state_label.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        return


    def on_tab1_left_picutre_navigate_button_clicked(self):
        self.tab1_pictureNavigateCount = self.tab1_pictureNavigateCount - 1
        
        self.update_pictures(self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount],
                            self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount].replace(self.tab1_originalPictureDirectoryPath, self.tab1_detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab1_left_picture,
                            self.tab1_right_picture)
        
        if self.tab1_pictureNavigateCount == 0:
            self.tab1_left_picture_navigate_button.setEnabled(False)
        
        if self.tab1_right_picture_navigate_button.isEnabled() == False:
            self.tab1_right_picture_navigate_button.setEnabled(True)
        
        return
            

    def on_tab1_right_picutre_navigate_button_clicked(self):
        self.tab1_pictureNavigateCount = self.tab1_pictureNavigateCount + 1

        self.update_pictures(self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount],
                            self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount].replace(self.tab1_originalPictureDirectoryPath, self.tab1_detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab1_left_picture,
                            self.tab1_right_picture)
        
        if self.tab1_pictureNavigateCount == len(self.tab1_originalPictureAddresses) - 1:
            self.tab1_right_picture_navigate_button.setEnabled(False)
        
        if self.tab1_left_picture_navigate_button.isEnabled() == False:
            self.tab1_left_picture_navigate_button.setEnabled(True)
                
        return

    
    def on_tab2_comboBox_changed(self):
        self.tab2_statistical_data_label.clear()
        self.tab2_date_label.clear()
        self.tab2_left_picture.clear()
        self.tab2_right_picture.clear()
        self.tab2_orchard_comboBox.setEnabled(False)
        self.tab2_left_picture_navigate_button.setEnabled(False)
        self.tab2_right_picture_navigate_button.setEnabled(False)
        self.tab2_left_date_navigate_button.setEnabled(False)
        self.tab2_right_date_navigate_button.setEnabled(False)
        self.tab2_outputNavigateCount = 0
        self.tab2_detectionOutputPaths = []

        self.tab2_state_label.setText(self.tr('Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        collect_output_paths_return = self.tab2_collect_output_paths()

        if collect_output_paths_return == 1 or collect_output_paths_return == 2:
            self.tab2_orchard_comboBox.setEnabled(True)
            self.tab2_date_label.setText(self.tr('No data to show'))
            self.tab2_state_label.setText(self.tr('Ready'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            return

        f = open(self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount] + 'statistics.json')
        openedStatisticalData = json.load(f)
        f.close()

        self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']

        self.tab2_update_statistical_data(openedStatisticalData)

        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture,
                            self.tab2_right_picture)

        self.tab2_orchard_comboBox.setEnabled(True)
        if len(self.tab2_detectionOutputPaths) > 1:
                self.tab2_right_date_navigate_button.setEnabled(True)
            
        if len(self.tab2_originalPictureAddresses) > 1:
            self.tab2_right_picture_navigate_button.setEnabled(True)
    
        self.tab2_state_label.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return
    

    def on_tab2_left_date_navigate_button_clicked(self):
        self.tab2_state_label.setText(self.tr('Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        self.tab2_outputNavigateCount = self.tab2_outputNavigateCount - 1

        f = open(self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount] + 'statistics.json')
        openedStatisticalData = json.load(f)
        f.close()

        self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']

        self.tab2_update_statistical_data(openedStatisticalData)

        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture,
                            self.tab2_right_picture)

        if self.tab2_outputNavigateCount == 0:
            self.tab2_left_date_navigate_button.setEnabled(False)
        
        if self.tab2_right_date_navigate_button.isEnabled() == False:
            self.tab2_right_date_navigate_button.setEnabled(True)

        self.tab2_state_label.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return
    

    def on_tab2_right_date_navigate_button_clicked(self):
        self.tab2_state_label.setText(self.tr('Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        self.tab2_outputNavigateCount = self.tab2_outputNavigateCount + 1

        f = open(self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount] + 'statistics.json')
        openedStatisticalData = json.load(f)
        f.close()

        self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']

        self.tab2_update_statistical_data(openedStatisticalData)

        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture,
                            self.tab2_right_picture)

        if self.tab2_outputNavigateCount == len(self.tab2_detectionOutputPaths) - 1:
            self.tab2_right_date_navigate_button.setEnabled(False)
        
        if self.tab2_left_date_navigate_button.isEnabled() == False:
            self.tab2_left_date_navigate_button.setEnabled(True)

        self.tab2_state_label.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return

    
    def on_tab2_left_picutre_navigate_button_clicked(self):
        self.tab2_pictureNavigateCount = self.tab2_pictureNavigateCount - 1
        
        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture,
                            self.tab2_right_picture)
        
        if self.tab2_pictureNavigateCount == 0:
            self.tab2_left_picture_navigate_button.setEnabled(False)
        
        if self.tab2_right_picture_navigate_button.isEnabled() == False:
            self.tab2_right_picture_navigate_button.setEnabled(True)
        
        return
            

    def on_tab2_right_picutre_navigate_button_clicked(self):
        self.tab2_pictureNavigateCount = self.tab2_pictureNavigateCount + 1

        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_outputNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture,
                            self.tab2_right_picture)
        
        if self.tab2_pictureNavigateCount == len(self.tab2_originalPictureAddresses) - 1:
            self.tab2_right_picture_navigate_button.setEnabled(False)
        
        if self.tab2_left_picture_navigate_button.isEnabled() == False:
            self.tab2_left_picture_navigate_button.setEnabled(True)
                
        return

    
    def tab2_update_statistical_data(self, openedStatisticalData):
        self.tab2_originalPictureAddresses = []
        self.tab2_pictureNavigateCount = 0

        self.tab2_date_label.setText(self.tr(openedStatisticalData['time'] + ' , at ' + openedStatisticalData['orchard']))

        self.tab2_statistical_data_label.setText(self.tr(
                        'DOMINANT OBJECT: ' + openedStatisticalData['dominant_object'].upper() + '\n' + \
                        'egg: ' + str(openedStatisticalData['objects_count']['egg']) + '    ' + \
                        'larval_before: ' + str(openedStatisticalData['objects_count']['larval_before']) + '    ' + \
                        'larval_after: ' + str(openedStatisticalData['objects_count']['larval_after']) + '    ' + \
                        'juvenile: ' + str(openedStatisticalData['objects_count']['juvenile']) + '    ' + \
                        'tessaratoma: ' + str(openedStatisticalData['objects_count']['tessaratoma'])
        ))

        for f in os.listdir(openedStatisticalData['detected_directory']):
            if (f.lower().__contains__('.jpg')):
                self.tab2_originalPictureAddresses.append(openedStatisticalData['detected_directory'] + f)
            elif (f.lower().__contains__('.jpeg')):
                self.tab2_originalPictureAddresses.append(openedStatisticalData['detected_directory'] + f)
            elif (f.lower().__contains__('.png')):
                self.tab2_originalPictureAddresses.append(openedStatisticalData['detected_directory'] + f)
        
        self.tab2_originalPictureAddresses.sort()
        
        return
    

    def tab2_collect_output_paths(self):
        orchardName = self.tab2_orchard_comboBox.currentText().replace(' ', '_')
        detectionOutputDirectory = os.path.abspath('.') + '/detection_output'
        
        if os.path.exists(detectionOutputDirectory) is False:
            return 1
        
        for p in os.listdir(os.path.abspath('.') + '/detection_output'):
            if (p.__contains__(orchardName)):
                self.tab2_detectionOutputPaths.append(detectionOutputDirectory + '/' + p + '/')
        
        self.tab2_detectionOutputPaths.sort(reverse=True)

        if len(self.tab2_detectionOutputPaths) == 0:
            return 1
        
        return 0

        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
