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
        MainWindow.resize(960, 720)
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

        # Tab1 -  test demo
        self.centralwidget = QtWidgets.QWidget(MainWindow) # parent is MainWindow
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget) # parent is centralWidget
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 960, 720))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget() # declaration for tab, no inheritance needed
        self.tab1.setObjectName("tab1")
        
        # Label for selecting picture instructions
        self.tab1_picture_label = QtWidgets.QLabel(self.tab1)
        self.tab1_picture_label.setObjectName("tab1_picture_label")
        self.tab1_picture_label_font = QtGui.QFont()
        self.tab1_picture_label_font.setPointSize(14)
        self.tab1_picture_label.setFont(self.tab1_picture_label_font)
        
        # Button for selecting picture
        self.tab1_picture_button = QtWidgets.QPushButton(self.tab1)  # parent is tab, which declares at line 26
        self.tab1_picture_button.setFixedWidth(120)
        self.tab1_picture_button.setMouseTracking(True)
        self.tab1_picture_button.setObjectName("tab1_picture_button")

        # Text for showing the path of the pic
        self.tab1_picture_path_lineEdit = QtWidgets.QLineEdit(self.tab1) # parent is tab
        self.tab1_picture_path_lineEdit.setObjectName("tab1_picture_path_lineEdit")
        self.tab1_picture_path = ''
        
        # Running state
        self.tab1_state = QtWidgets.QLabel(self.tab1)
        self.tab1_state.setObjectName("tab1_state")

        # Button for performing the test
        self.tab1_test_button = QtWidgets.QPushButton(self.tab1) # parent is tab
        self.tab1_test_button.setMouseTracking(True)
        self.tab1_test_button.setObjectName("tab1_test_button")

        # Seperate line for buttons and pictures
        self.tab1_line = QtWidgets.QFrame(self.tab1) # parent is tab
        self.tab1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab1_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab1_line.setObjectName("tab1_line")

        # Label for showing statistics data
        self.tab1_statistics_data_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistics_data_label.setFixedHeight(57)
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
        self.tab1_left_picture = QtWidgets.QLabel(self.tab1)
        self.tab1_left_picture.setObjectName("tab1_left_picture")
        self.tab1_left_picture.setFixedHeight(400)
        self.tab1_left_picture.setFixedWidth(420)
        #self.gridLayout.addWidget(self.tab1_left_picture, 0, 0, 1, 1)
        self.tab1_left_picture_navigate_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_left_picture_navigate_button.setEnabled(False)
        self.tab1_left_picture_navigate_button.setMouseTracking(True)
        self.tab1_left_picture_navigate_button.setFixedWidth(51)
        self.tab1_left_picture_navigate_button.setFixedHeight(400)
        self.tab1_left_picture_navigate_button.setObjectName("tab1_left_picture_navigate_button")
        
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
        self.tab1_right_picture.setFixedHeight(400)
        self.tab1_right_picture.setFixedWidth(420)
        #self.gridLayout_2.addWidget(self.tab1_right_picture, 0, 0, 1, 1)
        self.tab1_right_picture_navigate_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_right_picture_navigate_button.setEnabled(False)
        self.tab1_right_picture_navigate_button.setMouseTracking(True)
        self.tab1_right_picture_navigate_button.setFixedWidth(51)
        self.tab1_right_picture_navigate_button.setFixedHeight(400)
        self.tab1_right_picture_navigate_button.setObjectName("tab1_right_picture_navigate_button")

        self.tab1_picture_navigate_button_font = QtGui.QFont()
        self.tab1_picture_navigate_button_font.setPointSize(14)
        self.tab1_left_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)
        self.tab1_right_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)

        # Nesting layout
        self.tab1_verticalLayout = QtWidgets.QVBoxLayout(self.tab1)  # parent is tab. In order to line up widgets under self.tab1???
        self.tab1_picture_instruction_widget = QtWidgets.QWidget()
        self.tab1_picture_instruction_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_instruction_widget)
        self.tab1_picture_selection_widget = QtWidgets.QWidget()
        self.tab1_picture_selection_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_selection_widget)  # parent is tab. In order to line up widgets under tab1_picture_path_widget???
        self.tab1_test_widget = QtWidgets.QWidget()
        self.tab1_test_widget_layout = QtWidgets.QVBoxLayout(self.tab1_test_widget)  # parent is tab. In order to line up widgets under tab1_test_widget???
        self.tab1_statistics_data_widget = QtWidgets.QWidget()
        self.tab1_statistics_data_widget_layout = QtWidgets.QHBoxLayout(self.tab1_statistics_data_widget)
        self.tab1_picture_widget = QtWidgets.QWidget()
        self.tab1_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_widget) # parent is tab. In order to line up widgets under tab1_picture_widget???

        # picture path widget
        self.tab1_picture_instruction_widget_layout.addWidget(self.tab1_picture_label)

        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_button)
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_path_lineEdit)

        # detection widget
        self.tab1_test_widget_layout.addWidget(self.tab1_test_button)
        self.tab1_test_widget_layout.addWidget(self.tab1_state)

        # statistics data widget
        self.tab1_statistics_data_widget_layout.addWidget(self.tab1_statistics_data_label)

        # pichture showing widget
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture_navigate_button)
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture_navigate_button)
        self.tab1_picture_widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # whole layout
        self.tab1_verticalLayout.addWidget(self.tab1_picture_instruction_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_selection_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_test_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_line)
        self.tab1_verticalLayout.addWidget(self.tab1_statistics_data_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_widget)
        self.tab1_verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        
        # Add tab1 and things above into the tabWidget
        self.tabWidget.addTab(self.tab1, "")
        '''
        # Tab2 - preprocessing
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        # Left grid for original picture
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(240, 130, 201, 191))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tab2_left_picture = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.tab2_left_picture.setObjectName("tab2_left_picture")
        self.gridLayout_3.addWidget(self.tab2_left_picture, 0, 0, 1, 1)
        
        # Right grid for transformed picture
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 130, 201, 191))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tab2_right_picture = QtWidgets.QGraphicsView(self.gridLayoutWidget_4)
        self.tab2_right_picture.setObjectName("tab2_right_picture")
        self.gridLayout_4.addWidget(self.tab2_right_picture, 0, 0, 1, 1)
        
        # Seperate line for buttons and pictures
        self.tab2_line = QtWidgets.QFrame(self.tab_2)
        self.tab2_line.setGeometry(QtCore.QRect(0, 40, 461, 16))
        self.tab2_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab2_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab2_line.setObjectName("tab2_line")
        
        # Button for selecting the picture
        self.tab2_pic_button = QtWidgets.QPushButton(self.tab_2)
        self.tab2_pic_button.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.tab2_pic_button.setMouseTracking(True)
        self.tab2_pic_button.setObjectName("tab2_pic_button")
        # Text for showing the path of the pic
        self.tab2_pic_path = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_pic_path.setGeometry(QtCore.QRect(110, 10, 331, 21))
        self.tab2_pic_path.setObjectName("tab2_pic_path")
        
        # Button for performing the transformation
        self.tab2_transformation_button = QtWidgets.QPushButton(self.tab_2)
        self.tab2_transformation_button.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.tab2_transformation_button.setMouseTracking(True)
        self.tab2_transformation_button.setObjectName("tab2_transformation_button")
        '''
        '''
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_4 = QtWidgets.QLineEdit(self.tab_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 60, 331, 21))
        self.textBrowser_4.setObjectName("textBrowser_4")
        '''
        
        #self.tabWidget.addTab(self.tab_2, "")
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
        self.tab1_picture_label.setText(_translate("MainWindow", "Click \"Browse\" to select the directory containing the pictures to detect"))
        self.tab1_picture_button.setText(_translate("MainWindow", "Browse"))
        self.tab1_test_button.setText(_translate("MainWindow", "Detect"))
        self.tab1_state.setText(_translate("MainWindow", "Ready"))
        self.tab1_left_picture_navigate_button.setText(_translate("MainWindow", "<"))
        self.tab1_right_picture_navigate_button.setText(_translate("MainWindow", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Detection"))
        
        # tab 2
        #self.tab2_pic_button.setText(_translate("MainWindow", "Select PIC"))
        #self.tab2_transformation_button.setText(_translate("MainWindow", "Transform!"))
        #self.pushButton_5.setText(_translate("MainWindow", "Mode"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data Augmentation Demo"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QtWidgets.QMainWindow.__init__(self)

        # Initialize UI
        self.setupUi(self)
        # Signal Setting
        self.tab1_picture_button.clicked.connect(self.on_tab1_picture_button_Clicked)
        self.tab1_test_button.clicked.connect(self.on_tab1_test_button_Clicked)
        self.tab1_left_picture_navigate_button.clicked.connect(self.on_tab1_left_picutre_navigate_button_Clicked)
        self.tab1_right_picture_navigate_button.clicked.connect(self.on_tab1_right_picutre_navigate_button_Clicked)

        # variables for showing pictures
        self.navigateCount = 0
        self.originalPictureAddresses = []
        self.detectedPictureAddresses = []


    def tr(self, text):
        return QtCore.QObject.tr(self, text)


    def on_tab1_picture_button_Clicked(self):
        source = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr('Open directory'), '/home/mmnlab/')
        if source:
            self.tab1_picture_path_lineEdit.setText(source)
            self.tab1_picture_path = source
            self.tab1_state.setText(self.tr('Selected directory: ' + source))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        elif source == '':
            if self.tab1_picture_path_lineEdit.text() == '':
                self.tab1_state.setText(self.tr('No directory selected'))
                QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        return


    def on_tab1_test_button_Clicked(self):
        if self.tab1_picture_path == '':
            print("No directory selected")
            self.tab1_state.setText(self.tr('No directory selected'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            return
        
        # collecting paths to all the pictures waiting to run detection
        self.tab1_state.setText(self.tr('Collecting paths'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        for f in os.listdir(self.tab1_picture_path):
            if (f.lower().__contains__('.jpg')):
                self.originalPictureAddresses.append(self.tab1_picture_path + '/' + f)
            elif (f.lower().__contains__('.jpeg')):
                self.originalPictureAddresses.append(self.tab1_picture_path + '/' + f)
            elif (f.lower().__contains__('.png')):
                self.originalPictureAddresses.append(self.tab1_picture_path + '/' + f)
        
        self.originalPictureAddresses.sort()

        # make directory to store detected samples and detection log
        detectionOutputPath = os.path.abspath('.') + '/detection_output/'
        if os.path.isdir(detectionOutputPath) is False:
            os.mkdir(detectionOutputPath)
            self.tab1_state.setText(self.tr('Created directory: ' + detectionOutputPath))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        else:
            self.tab1_state.setText(self.tr('Directory: ' + detectionOutputPath + ' already existed'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        resultDirectoryName = date.replace('/', '').replace(':', '').replace(' ', '_')
        
        detectionOutputPath = detectionOutputPath + resultDirectoryName + '/'
        os.mkdir(detectionOutputPath)

        self.tab1_state.setText(self.tr('Created directory: ' + detectionOutputPath))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # create empty detection log file
        commands = ['touch',
                    detectionOutputPath + 'detection_results.json']
        os.system(' '.join(commands))

        self.tab1_state.setText(self.tr('Detection log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        # create empty statistics log file
        commands = ['touch',
                    detectionOutputPath + 'statistics.json']
        os.system(' '.join(commands))

        self.tab1_state.setText(self.tr('Statistics log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # run detection
        ### batch images detector (darknet) provided by vincentgong7 ###
        self.tab1_state.setText(self.tr('Detection started, please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        commands = ['./darknet detector batch',
                    'data/obj.data',
                    'cfg/yolov4-custom.cfg',
                    'weights/20200509_20000iterations_random0_sub32_wh480/yolov4-custom_20000.weights',
                    'io_folder ' + self.tab1_picture_path + '/',
                    detectionOutputPath,
                    '-out ' + detectionOutputPath + '/detection_results.json',
                    '-dont_show']
        os.system(' '.join(commands))
        self.tab1_state.setText(self.tr('Detection finished'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # collecting paths to all the detected pictures
        for f in os.listdir(detectionOutputPath):
            if (f.lower().__contains__('.jpg')):
                self.detectedPictureAddresses.append(detectionOutputPath + '/' + f)
            elif (f.lower().__contains__('.jpeg')):
                self.detectedPictureAddresses.append(detectionOutputPath + '/' + f)
            elif (f.lower().__contains__('.png')):
                self.detectedPictureAddresses.append(detectionOutputPath + '/' + f)
        
        self.detectedPictureAddresses.sort()

        # statistics data
        self.tab1_state.setText(self.tr('Generating statistics data'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        detectedObjectCount = [0, 0, 0, 0, 0]

        f = open(detectionOutputPath + 'detection_results.json')
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
            "detection_output_path": detectionOutputPath,
            "detected_directory": self.tab1_picture_path,
            "dominant_object": dominantObject,
            "objects_count": {"egg": detectedObjectCount[0], "larval_before": detectedObjectCount[1], "larval_after": detectedObjectCount[2], "juvenile": detectedObjectCount[3], "tessaratoma": detectedObjectCount[4]}
        }

        with open(detectionOutputPath + 'statistics.json', 'w') as outfile:
            outfile.write(json.dumps(statisticsDictionary, indent=4))
        
        self.tab1_state.setText(self.tr('Statistics data saved successfully'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # show statistics data in message box
        statisticsDataToShow = 'Time: ' + date + '\n' + \
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
        left_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount])
        left_pixmap = left_pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_left_picture.setPixmap(left_pixmap)
        right_pixmap = QtGui.QPixmap(self.detectedPictureAddresses[self.navigateCount])
        right_pixmap = right_pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_right_picture.setPixmap(right_pixmap)

        statisticsDataMessage = QtWidgets.QMessageBox()
        statisticsDataMessage.setWindowTitle(self.tr('Statistic result'))
        statisticsDataMessage.setText(self.tr('DOMINANT OBJECT: ' + dominantObject.upper()))
        statisticsDataMessage.setInformativeText(self.tr(statisticsDataToShow))
        statisticsDataMessage.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        statisticsDataMessage.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)

        statisticsDataMessage.exec()

        self.tab1_left_picture_navigate_button.setEnabled(True)
        self.tab1_right_picture_navigate_button.setEnabled(True)

        print(self.tab1_statistics_data_label.geometry())

        self.tab1_state.setText(self.tr('Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        return


    def on_tab1_left_picutre_navigate_button_Clicked(self):
        if self.navigateCount == 0:
            return
        else:
            self.navigateCount = self.navigateCount - 1
            left_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount])
            left_pixmap = left_pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.tab1_left_picture.setPixmap(left_pixmap)
            right_pixmap = QtGui.QPixmap(self.detectedPictureAddresses[self.navigateCount])
            right_pixmap = right_pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.tab1_right_picture.setPixmap(right_pixmap)
        return
            

    def on_tab1_right_picutre_navigate_button_Clicked(self):
        if self.navigateCount == len(self.detectedPictureAddresses) - 1:
            return
        else:
            self.navigateCount = self.navigateCount + 1
            left_pixmap = QtGui.QPixmap(self.originalPictureAddresses[self.navigateCount])
            left_pixmap = left_pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.tab1_left_picture.setPixmap(left_pixmap)
            right_pixmap = QtGui.QPixmap(self.detectedPictureAddresses[self.navigateCount])
            right_pixmap = right_pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.tab1_right_picture.setPixmap(right_pixmap)
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
