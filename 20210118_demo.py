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
        MainWindow.resize(1280, 720)

        # Tab1 -  test demo
        self.centralwidget = QtWidgets.QWidget(MainWindow) # parent is MainWindow
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget) # parent is centralWidget
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget() # declaration for tab, no inheritance needed
        self.tab.setObjectName("tab")
        
        # Left grid for original picture
        '''
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 201, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        '''
        self.tab1_left_picture = QtWidgets.QLabel(self)
        self.tab1_left_picture.setObjectName("tab1_left_picture")
        #self.gridLayout.addWidget(self.tab1_left_picture, 0, 0, 1, 1)
        
        # Right grid for detected picture
        '''
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(240, 90, 201, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        '''
        self.tab1_right_picture = QtWidgets.QLabel(self)
        self.tab1_right_picture.setObjectName("tab1_right_picture")
        #self.gridLayout_2.addWidget(self.tab1_right_picture, 0, 0, 1, 1)
        
        # Button for selecting picture
        self.tab1_picture_button = QtWidgets.QPushButton(self.tab) # parent is tab, which declares at line 26
        #self.tab1_picture_button.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.tab1_picture_button.setMouseTracking(True)
        self.tab1_picture_button.setObjectName("tab1_picture_button")
        # Text for showing the path of the pic
        self.tab1_picture_path_lineEdit = QtWidgets.QLineEdit(self.tab) # parent is tab
        #self.tab1_picture_path_lineEdit.setGeometry(QtCore.QRect(110, 40, 331, 21))
        self.tab1_picture_path_lineEdit.setObjectName("tab1_picture_path_lineEdit")
        self.tab1_picture_path = ''
        
        # Button for selecting model
        '''self.tab1_model_button = QtWidgets.QPushButton(self.tab) # parent is tab
        #self.tab1_model_button.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.tab1_model_button.setMouseTracking(True)
        self.tab1_model_button.setObjectName("tab1_model_button")
        # Text for showing the path of the model
        self.tab1_model_path = QtWidgets.QLineEdit(self.tab) # parent is tab
        #self.tab1_model_path.setGeometry(QtCore.QRect(110, 10, 331, 21))
        self.tab1_model_path.setObjectName("tab1_model_path")
        self.tab1_model = '''''
        
        # Running state
        self.tab1_state = QtWidgets.QLabel(self.tab)
        self.tab1_state.setObjectName("tab1_state")
        
        # Seperate line for buttons and pictures
        self.tab1_line = QtWidgets.QFrame(self.tab) # parent is tab
        #self.tab1_line.setGeometry(QtCore.QRect(0, 70, 461, 16))
        self.tab1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab1_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab1_line.setObjectName("tab1_line")

        # Button for performing the test
        self.tab1_test_button = QtWidgets.QPushButton(self.tab) # parent is tab
        #self.tab1_test_button.setGeometry(QtCore.QRect(370, 290, 75, 23))
        self.tab1_test_button.setMouseTracking(True)
        self.tab1_test_button.setObjectName("tab1_test_button")

        # Nesting layout
        self.tab1_verticalLayout = QtWidgets.QVBoxLayout(self.tab) # parent is tab. In order to line up widgets under self.tab???
        # self.tab1_model_widget = QtWidgets.QWidget()
        # self.tab1_model_widget_layout = QtWidgets.QHBoxLayout(self.tab1_model_widget) # parent is tab. In order to line up widgets under tab1_model_widget???
        self.tab1_picture_path_widget = QtWidgets.QWidget()
        self.tab1_picture_path_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_path_widget) # parent is tab. In order to line up widgets under tab1_picture_path_widget???
        self.tab1_picture_widget = QtWidgets.QWidget()
        self.tab1_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_widget) # parent is tab. In order to line up widgets under tab1_picture_widget???
        self.tab1_test_widget = QtWidgets.QWidget()
        self.tab1_test_widget_layout = QtWidgets.QVBoxLayout(self.tab1_test_widget) # parent is tab. In order to line up widgets under tab1_test_widget???

        # add widget objects to layout object
        # self.tab1_model_widget_layout.addWidget(self.tab1_model_button)
        # self.tab1_model_widget_layout.addWidget(self.tab1_model_path)

        self.tab1_picture_path_widget_layout.addWidget(self.tab1_picture_button)
        self.tab1_picture_path_widget_layout.addWidget(self.tab1_picture_path_lineEdit)

        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture)

        self.tab1_test_widget_layout.addWidget(self.tab1_test_button)
        self.tab1_test_widget_layout.addWidget(self.tab1_state)

        # self.tab1_verticalLayout.addWidget(self.tab1_model_widget, alignment=QtCore.Qt.AlignTop)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_path_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_test_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_line)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_widget)

        self.tab1_verticalLayout.setAlignment(QtCore.Qt.AlignTop)
        
        # Add tab1 and things above into the tabWidget
        self.tabWidget.addTab(self.tab, "")
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
        self.tab1_picture_button.setText(_translate("MainWindow", "Select dir"))
        # self.tab1_model_button.setText(_translate("MainWindow", "Select Model"))
        self.tab1_test_button.setText(_translate("MainWindow", "Detect"))
        self.tab1_state.setText(_translate("MainWindow", "Ready"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Model Test Demo"))
        
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
        # self.tab1_model_button.clicked.connect(self.on_tab1_model_button_Clicked)
        self.tab1_test_button.clicked.connect(self.on_tab1_test_button_Clicked)

        self.serialNumberCount = 0
        self.originalPictureAddresses = []
        self.detectedPictureAddresses = []

    def tr(self, text):
        return QtCore.QObject.tr(self, text)

    def on_tab1_picture_button_Clicked(self):
        path_to_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
                self.tr("Load Image"), self.tr("~/Desktop/"), self.tr("Images (*.jpg)"))
        '''if path_to_file:
            self.tab1_picture_path_lineEdit.setText(path_to_file)
            left_pixmap = QtGui.QPixmap(path_to_file)
            left_pixmap = left_pixmap.scaled(550, 225, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.tab1_left_picture.setPixmap(left_pixmap)
            self.tab1_picture_path = path_to_file'''
        if path_to_file == '':
            print("Nothing.")
            self.tab1_state.setText(self.tr('No directory selected'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            return
    
    '''def on_tab1_model_button_Clicked(self):
        path_to_file, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                self.tr("Load Model"), self.tr("~/Desktop/"), self.tr("Models (*.weights)"))
        if path_to_file:
            self.tab1_model_path.setText(path_to_file)
            self.tab1_model = path_to_file
        elif path_to_file == "":
            print("Nothing.")
            return'''

    def on_tab1_test_button_Clicked(self):
        '''if self.tab1_model == '':
            print("No model!")
            return'''
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

        darknetPath = 'github_repositories/VG_AlexeyAB_darknet/'
        # make directory to store detected samples and detection log
        self.tab1_state.setText(self.tr('Creating output directory'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        detectionOutputPath = os.path.abspath('.') + '/detection_output/'
        if os.path.isdir(detectionOutputPath) is False:
            os.mkdir(detectionOutputPath)
        
        # generate serial number
        date = datetime.now().strftime("%Y%m%d")
        serialNumber = date + '{0:03}'.format(self.serialNumberCount)
        while (os.path.isdir(detectionOutputPath + serialNumber) is False):
            self.serialNumberCount = self.serialNumberCount + 1
            serialNumber = date + '{0:03}'.format(self.serialNumberCount)
        
        detectionOutputPath = detectionOutputPath + serialNumber
        os.mkdir(detectionOutputPath)

        # create empty detection log file
        commands = ['touch',
                    detectionOutputPath + '/detection_results.json']
        os.system(' '.join(commands))
        # create empty statistics log file
        commands = ['touch',
                    detectionOutputPath + '/statistics.json']
        os.system(' '.join(commands))

        '''movie = QtGui.QMovie('loading.gif')
        movie.setCacheMode(QtGui.QMovie.CacheAll)
        movie.setSpeed(100)
        movie.setScaledSize(QtCore.QSize(50,50))
        self.tab1_state.setMovie(movie)
        movie.start()'''

        # run detection
        ### batch images detector (darknet) provided by vincentgong7 ###
        self.tab1_state.setText(self.tr('Start detection'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        commands = ['./' + darknetPath + 'darknet detector batch',
                    darknetPath + 'data/obj.data',
                    darknetPath + 'cfg/yolov4-custom.cfg',
                    darknetPath + 'backup/20200509_20000iterations_random0_sub32_wh480/yolov4-custom_20000.weights',
                    'io_folder ' + self.tab1_picture_path,
                    detectionOutputPath,
                    '-out ' + detectionOutputPath + '/detection_results.json',
                    '-dont_show -ext_output']
        os.system(' '.join(commands))

        # collecting paths to all the detected pictures
        for f in os.listdir(detectionOutputPath):
            if (f.lower().__contains__('.jpg')):
                self.detectedPictureAddresses.append(detectionOutputPath + '/' + f)
            elif (f.lower().__contains__('.jpeg')):
                self.detectedPictureAddresses.append(detectionOutputPath + '/' + f)
            elif (f.lower().__contains__('.png')):
                self.detectedPictureAddresses.append(detectionOutputPath + '/' + f)
        
        self.detectedPictureAddresses.sort()

        '''img_path = "/home/mmnlab/Desktop/joey/20200430/darknet/predictions.jpg"
        right_pixmap = QtGui.QPixmap(img_path)
        right_pixmap = right_pixmap.scaled(550, 225, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_right_picture.setPixmap(right_pixmap)'''
        
        '''check = 'check.jpg'
        state_pixmap = QtGui.QPixmap(check)
        state_pixmap = state_pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_state.setPixmap(state_pixmap)'''





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
