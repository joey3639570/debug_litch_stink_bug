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
        self.tab1_orchard_label = QtWidgets.QLabel(self.tab1)
        self.tab1_orchard_label.setObjectName("tab1_orchard_label")
        self.tab1_orchard_label_font = QtGui.QFont()
        self.tab1_orchard_label_font.setPointSize(12)
        self.tab1_orchard_label.setFont(self.tab1_orchard_label_font)

        # ComboBox for selecting orchard
        self.tab1_orchard_comboBox = QtWidgets.QComboBox(self.tab1)
        self.tab1_orchard_comboBox.setObjectName('tab1_orchard_comboBox')
        self.tab1_orchard_comboBox.addItem('Orchard 1')
        self.tab1_orchard_comboBox.addItem('Orchard 2')
        self.tab1_orchard_comboBox.addItem('Orchard 3')
        
        # Instructions for selecting picture
        self.tab1_picture_label = QtWidgets.QLabel(self.tab1)
        self.tab1_picture_label.setObjectName("tab1_picture_label")
        self.tab1_picture_label_font = QtGui.QFont()
        self.tab1_picture_label_font.setPointSize(12)
        self.tab1_picture_label.setFont(self.tab1_picture_label_font)
        
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

        # Label for showing statistics data
        self.tab1_statistics_data_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistics_data_label.setFixedHeight(71)
        self.tab1_statistics_data_label.setObjectName("tab1_statistics_data_label")

        # Left grid for original picture
        '''
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 201, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        '''
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
        '''
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(240, 90, 201, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        '''
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
        self.tab1_statistics_data_widget = QtWidgets.QWidget()
        self.tab1_statistics_data_widget_layout = QtWidgets.QHBoxLayout(self.tab1_statistics_data_widget)
        self.tab1_picture_widget = QtWidgets.QWidget()
        self.tab1_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_widget) # parent is tab. In order to line up widgets under tab1_picture_widget???

        # orchard widget
        self.tab1_orchard_widget_layout.addWidget(self.tab1_orchard_comboBox)

        # picture path widget
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_button)
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_path_lineEdit)

        # detection widget
        self.tab1_test_widget_layout.addWidget(self.tab1_test_button)
        self.tab1_test_widget_layout.addWidget(self.tab1_state_label)

        # statistics data widget
        self.tab1_statistics_data_widget_layout.addWidget(self.tab1_statistics_data_label)

        # pichture showing widget
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture_navigate_button)
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture_navigate_button)
        self.tab1_picture_widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # whole layout
        self.tab1_verticalLayout.addWidget(self.tab1_orchard_label)
        self.tab1_verticalLayout.addWidget(self.tab1_orchard_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_label)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_selection_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_test_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_line)
        self.tab1_verticalLayout.addWidget(self.tab1_statistics_data_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_widget)
        self.tab1_verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        
        # Add tab1 and things above into the tabWidget
        self.tabWidget.addTab(self.tab1, "")
        

        # Tab2 - records
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        
        # Instructions for selecting orchard
        self.tab2_orchard_label = QtWidgets.QLabel(self.tab2)
        self.tab2_orchard_label.setObjectName("tab2_orchard_label")
        self.tab2_orchard_label_font = QtGui.QFont()
        self.tab2_orchard_label_font.setPointSize(12)
        self.tab2_orchard_label.setFont(self.tab1_orchard_label_font)

        # ComboBox for selecting orchard
        self.tab2_orchard_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_orchard_comboBox.setObjectName('tab2_orchard_comboBox')
        self.tab2_orchard_comboBox.addItem('Orchard 1')
        self.tab2_orchard_comboBox.addItem('Orchard 2')
        self.tab2_orchard_comboBox.addItem('Orchard 3')

        # Running state
        self.tab2_state_label = QtWidgets.QLabel(self.tab2)
        self.tab2_state_label.setObjectName('tab2_state_label')
        
        # LineEdit for showing statistics data
        self.tab2_orchard_statistics_data_textEdit = QtWidgets.QTextEdit(self.tab2)
        self.tab2_orchard_statistics_data_textEdit.setReadOnly(True)
        self.tab2_orchard_statistics_data_textEdit.setObjectName('tab2_orchard_statistics_data_textEdit')
        self.tab2_orchard_statistics_data_textEdit.setFixedHeight(640)

        # nesting layout
        self.tab2_verticalLayout = QtWidgets.QVBoxLayout(self.tab2)  # parent is tab. In order to line up widgets under self.tab1???
        self.tab2_orchard_widget = QtWidgets.QWidget()
        self.tab2_orchard_widget_layout = QtWidgets.QVBoxLayout(self.tab2_orchard_widget)

        # orchard comboBox and lineEdit
        self.tab2_orchard_widget_layout.addWidget(self.tab2_orchard_comboBox)
        self.tab2_orchard_widget_layout.addWidget(self.tab2_state_label)
        self.tab2_orchard_widget_layout.addWidget(self.tab2_orchard_statistics_data_textEdit)
        self.tab2_orchard_widget_layout.setAlignment(QtCore.Qt.AlignTop)

        # whole layout
        self.tab2_verticalLayout.addWidget(self.tab2_orchard_label)
        self.tab2_verticalLayout.addWidget(self.tab2_orchard_widget)
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
        self.tab1_orchard_label.setText(_translate("MainWindow", "Select the orchard"))
        self.tab1_picture_label.setText(_translate("MainWindow", "Click \"Browse\" to select the directory containing the pictures to detect"))
        self.tab1_picture_button.setText(_translate("MainWindow", "Browse"))
        self.tab1_test_button.setText(_translate("MainWindow", "DETECT"))
        self.tab1_state_label.setText(_translate("MainWindow", "Ready"))
        self.tab1_left_picture_navigate_button.setText(_translate("MainWindow", "<"))
        self.tab1_right_picture_navigate_button.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Detection"))
        
        # tab 2
        self.tab2_orchard_label.setText(_translate("MainWindow", "Select the orchard"))
        self.tab2_state_label.setText(_translate("MainWindow", "Ready"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Statistics data"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QtWidgets.QMainWindow.__init__(self)

        # Initialize UI
        self.setupUi(self)
        # Signal Setting
        self.tabWidget.currentChanged['int'].connect(self.on_tabWidget_changed)

        self.tab1_picture_button.clicked.connect(self.on_tab1_picture_button_clicked)
        self.tab1_test_button.clicked.connect(self.on_tab1_test_button_clicked)
        self.tab1_left_picture_navigate_button.clicked.connect(self.on_tab1_left_picutre_navigate_button_clicked)
        self.tab1_right_picture_navigate_button.clicked.connect(self.on_tab1_right_picutre_navigate_button_clicked)
        
        self.tab2_orchard_comboBox.currentIndexChanged.connect(self.on_tab2_comboBox_changed)

        # variables for line edit style
        self.lineEditOriginalStyle = self.tab1_picture_path_lineEdit.styleSheet()

        # variables for showing pictures
        self.navigateCount = 0
        self.originalPictureAddresses = []
        self.detectionOutputPath = ''


    def on_tabWidget_changed(self, index):
        if index == 0:
            self.tab1_state_label.setText(self.tr('Ready'))
        elif index == 1:
            self.tab2_orchard_statistics_data_textEdit.clear()

            self.tab2_state_label.setText(self.tr('Loading. Please wait...'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

            orchardName = self.tab2_orchard_comboBox.currentText().replace(' ', '_')
            detectionOutputPath = os.path.abspath('.') + '/detection_output'
            
            if os.path.exists(detectionOutputPath) is False:
                self.tab2_orchard_statistics_data_textEdit.append(self.tr('No data to show'))
                self.tab2_state_label.setText(self.tr('Ready'))
                QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
                return

            detectionOutputs = os.listdir(detectionOutputPath)
            detectionOutputs.sort(reverse=True)

            statisticsDataAppended = 0
            for f in detectionOutputs:
                if (f.__contains__(orchardName)):
                    statisticsDataAppended = 1
                    f = open(detectionOutputPath + '/' + f + '/statistics.json')
                    openedStatisticsData = json.load(f)

                    self.tab2_orchard_statistics_data_textEdit.append(self.tr(
                                 'Time: ' + openedStatisticsData['time'] + '\n' + \
                                 'Orchard: ' + openedStatisticsData['orchard'] + '\n' + \
                                 'DOMINANT OBJECT: ' + openedStatisticsData['dominant_object'].upper() + '\n' + \
                                 'Object count: ' + '\n' + \
                                 '    ' + 'egg: ' + str(openedStatisticsData['objects_count']['egg']) + ' detected\n' + \
                                 '    ' + 'larval_before: ' + str(openedStatisticsData['objects_count']['larval_before']) + ' detected\n' + \
                                 '    ' + 'larval_after: ' + str(openedStatisticsData['objects_count']['larval_after']) + ' detected\n' + \
                                 '    ' + 'juvenile: ' + str(openedStatisticsData['objects_count']['juvenile']) + ' detected\n' + \
                                 '    ' + 'tessaratoma: ' + str(openedStatisticsData['objects_count']['tessaratoma']) + ' detected\n' + \
                                 '--------------------\n'
                    ))
                    f.close()
            
            self.tab2_orchard_statistics_data_textEdit.verticalScrollBar().setValue(0)

            if statisticsDataAppended == 0:
                self.tab2_orchard_statistics_data_textEdit.append(self.tr('No data to show'))
            
            self.tab2_state_label.setText(self.tr('Ready'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            
        return

    
    def tr(self, text):
        return QtCore.QObject.tr(self, text)


    def on_tab1_picture_button_clicked(self):
        source = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr('Open directory'), '/home/mmnlab/')
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

        # create directory to store detected samples and detection log
        self.detectionOutputPath = os.path.abspath('.') + '/detection_output/'
        if os.path.isdir(self.detectionOutputPath) is False:
            os.mkdir(self.detectionOutputPath)
            self.tab1_state_label.setText(self.tr('Directory: ' + self.detectionOutputPath + ' created'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        else:
            self.tab1_state_label.setText(self.tr('Directory: ' + self.detectionOutputPath + ' already existed'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        resultDirectoryName = self.tab1_orchard_comboBox.currentText().replace(' ', '_') + '_' + date.replace('/', '').replace(':', '').replace(' ', '_')
        self.detectionOutputPath = self.detectionOutputPath + resultDirectoryName + '/'
        os.mkdir(self.detectionOutputPath)

        self.tab1_state_label.setText(self.tr('Created directory: ' + self.detectionOutputPath))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # create empty detection log file
        commands = ['touch',
                    self.detectionOutputPath + 'detection_results.json']
        os.system(' '.join(commands))

        self.tab1_state_label.setText(self.tr('Detection log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        # create empty statistics log file
        commands = ['touch',
                    self.detectionOutputPath + 'statistics.json']
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
                    'io_folder ' + self.tab1_picture_path,
                    self.detectionOutputPath,
                    '-out ' + self.detectionOutputPath + 'detection_results.json',
                    '-dont_show']
        os.system(' '.join(commands))
        
        self.tab1_state_label.setText(self.tr('Detection finished'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # collecting paths to all the pictures waiting to run the detection
        self.originalPictureAddresses = []

        self.tab1_state_label.setText(self.tr('Collecting paths'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        for f in os.listdir(self.tab1_picture_path):
            if (f.lower().__contains__('.jpg')):
                self.originalPictureAddresses.append(self.tab1_picture_path + f)
            elif (f.lower().__contains__('.jpeg')):
                self.originalPictureAddresses.append(self.tab1_picture_path + f)
            elif (f.lower().__contains__('.png')):
                self.originalPictureAddresses.append(self.tab1_picture_path + f)
        
        self.originalPictureAddresses.sort()

        # statistics data
        self.tab1_state_label.setText(self.tr('Generating statistics data'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        detectedObjectCount = [0, 0, 0, 0, 0]

        f = open(self.detectionOutputPath + 'detection_results.json')
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
            "detection_output_path": self.detectionOutputPath  + 'detection_results.json',
            "detected_directory": self.tab1_picture_path,
            "dominant_object": dominantObject,
            "objects_count": {"egg": detectedObjectCount[0], "larval_before": detectedObjectCount[1], "larval_after": detectedObjectCount[2], "juvenile": detectedObjectCount[3], "tessaratoma": detectedObjectCount[4]}
        }

        with open(self.detectionOutputPath + 'statistics.json', 'w') as outfile:
            outfile.write(json.dumps(statisticsDictionary, indent=4))
        
        self.tab1_state_label.setText(self.tr('Statistics data saved successfully'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # show statistics data in message box
        statisticsDataToShow = 'Time: ' + date + '\n' + \
                                 'Orchard: ' + self.tab1_orchard_comboBox.currentText() + '\n' + \
                                 'DOMINANT OBJECT: ' + dominantObject.upper() + '\n' + \
                                 'Object count: ' + '\n' + \
                                 '    ' + 'egg: ' + str(detectedObjectCount[0]) + ' detected\n' + \
                                 '    ' + 'larval_before: ' + str(detectedObjectCount[1]) + ' detected\n' + \
                                 '    ' + 'larval_after: ' + str(detectedObjectCount[2]) + ' detected\n' + \
                                 '    ' + 'juvenile: ' + str(detectedObjectCount[3]) + ' detected\n' + \
                                 '    ' + 'tessaratoma: ' + str(detectedObjectCount[4]) + ' detected\n'

        # show statistics data in main window
        self.tab1_statistics_data_label.setText(QtCore.QCoreApplication.translate("MainWindow", statisticsDataToShow.replace('detected\n', 'detected')))

        # show pictures
        self.navigateCount = 0
        left_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount])
        left_pixmap = left_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_left_picture.setPixmap(left_pixmap)
        right_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount].replace(self.tab1_picture_path, self.detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'))
        right_pixmap = right_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_right_picture.setPixmap(right_pixmap)

        statisticsDataMessage = QtWidgets.QMessageBox()
        statisticsDataMessage.setWindowTitle(self.tr('Statistic result'))
        statisticsDataMessage.setInformativeText(self.tr(statisticsDataToShow))
        statisticsDataMessage.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        statisticsDataMessage.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)

        statisticsDataMessage.exec()

        self.tab1_right_picture_navigate_button.setEnabled(True)

        self.tab1_state_label.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        return


    def on_tab1_left_picutre_navigate_button_clicked(self):
        self.navigateCount = self.navigateCount - 1
        left_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount])
        left_pixmap = left_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_left_picture.setPixmap(left_pixmap)
        right_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount].replace(self.tab1_picture_path, self.detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'))
        right_pixmap = right_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_right_picture.setPixmap(right_pixmap)
        
        if self.navigateCount == 0:
            self.tab1_left_picture_navigate_button.setEnabled(False)
        
        if self.tab1_right_picture_navigate_button.isEnabled() == False:
            self.tab1_right_picture_navigate_button.setEnabled(True)
        
        return
            

    def on_tab1_right_picutre_navigate_button_clicked(self):
        self.navigateCount = self.navigateCount + 1
        left_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount])
        left_pixmap = left_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_left_picture.setPixmap(left_pixmap)
        right_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount].replace(self.tab1_picture_path, self.detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'))
        right_pixmap = right_pixmap.scaled(560, 416, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_right_picture.setPixmap(right_pixmap)
        
        if self.navigateCount == len(self.originalPictureAddresses) - 1:
            self.tab1_right_picture_navigate_button.setEnabled(False)
        
        if self.tab1_left_picture_navigate_button.isEnabled() == False:
            self.tab1_left_picture_navigate_button.setEnabled(True)
                
        return

    
    def on_tab2_comboBox_changed(self):
        self.tab2_orchard_statistics_data_textEdit.clear()

        self.tab2_state_label.setText(self.tr('Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        orchardName = self.tab2_orchard_comboBox.currentText().replace(' ', '_')
        detectionOutputPath = os.path.abspath('.') + '/detection_output'
        
        if os.path.exists(detectionOutputPath) is False:
            self.tab2_orchard_statistics_data_textEdit.append(self.tr('No data to show'))
            self.tab2_state_label.setText(self.tr('Ready'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            return

        detectionOutputs = os.listdir(detectionOutputPath)
        detectionOutputs.sort(reverse=True)

        statisticsDataAppended = 0
        for f in detectionOutputs:
            if (f.__contains__(orchardName)):
                statisticsDataAppended = 1
                f = open(os.path.abspath('.') + '/detection_output/' + f + '/statistics.json')
                openedStatisticsData = json.load(f)

                self.tab2_orchard_statistics_data_textEdit.append(self.tr(
                                'Time: ' + openedStatisticsData['time'] + '\n' + \
                                'Orchard: ' + openedStatisticsData['orchard'] + '\n' + \
                                'DOMINANT OBJECT: ' + openedStatisticsData['dominant_object'].upper() + '\n' + \
                                'Object count: ' + '\n' + \
                                '    ' + 'egg: ' + str(openedStatisticsData['objects_count']['egg']) + ' detected\n' + \
                                '    ' + 'larval_before: ' + str(openedStatisticsData['objects_count']['larval_before']) + ' detected\n' + \
                                '    ' + 'larval_after: ' + str(openedStatisticsData['objects_count']['larval_after']) + ' detected\n' + \
                                '    ' + 'juvenile: ' + str(openedStatisticsData['objects_count']['juvenile']) + ' detected\n' + \
                                '    ' + 'tessaratoma: ' + str(openedStatisticsData['objects_count']['tessaratoma']) + ' detected\n' + \
                                '--------------------\n'
                ))
                f.close()

        self.tab2_orchard_statistics_data_textEdit.verticalScrollBar().setValue(0)

        if statisticsDataAppended == 0:
            self.tab2_orchard_statistics_data_textEdit.append(self.tr('No data to show'))

        self.tab2_state_label.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
