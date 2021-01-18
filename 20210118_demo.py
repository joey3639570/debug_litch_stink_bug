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
        MainWindow.resize(800, 600)

        # Tab1 -  test demo
        self.centralwidget = QtWidgets.QWidget(MainWindow) # inherit from MainWindow
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget) # inherit from centralWidget
        self.tabWidget.setGeometry(QtCore.QRect(20, 25, 760, 550))
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
        self.tab1_left_pic = QtWidgets.QLabel(self)
        self.tab1_left_pic.setObjectName("tab1_left_pic")
        #self.gridLayout.addWidget(self.tab1_left_pic, 0, 0, 1, 1)
        
        # Right grid for detected picture
        '''
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(240, 90, 201, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        '''
        self.tab1_right_pic = QtWidgets.QLabel(self)
        self.tab1_right_pic.setObjectName("tab1_right_pic")
        #self.gridLayout_2.addWidget(self.tab1_right_pic, 0, 0, 1, 1)
        
        # Button for selecting picture
        self.tab1_pic_button = QtWidgets.QPushButton(self.tab) # inhereit from tab, which declares at line 26
        #self.tab1_pic_button.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.tab1_pic_button.setMouseTracking(True)
        self.tab1_pic_button.setObjectName("tab1_pic_button")
        # Text for showing the path of the pic
        self.tab1_pic_path = QtWidgets.QLineEdit(self.tab) # inhereit from tab
        #self.tab1_pic_path.setGeometry(QtCore.QRect(110, 40, 331, 21))
        self.tab1_pic_path.setObjectName("tab1_pic_path")
        self.tab1_pic = ''
        
        # Button for selecting model
        self.tab1_model_button = QtWidgets.QPushButton(self.tab) # inhereit from tab
        #self.tab1_model_button.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.tab1_model_button.setMouseTracking(True)
        self.tab1_model_button.setObjectName("tab1_model_button")
        # Text for showing the path of the model
        self.tab1_model_path = QtWidgets.QLineEdit(self.tab) # inhereit from tab
        #self.tab1_model_path.setGeometry(QtCore.QRect(110, 10, 331, 21))
        self.tab1_model_path.setObjectName("tab1_model_path")
        self.tab1_model = ''
        
        # Progressbar
        # self.tab1_state = QtWidgets.QLabel(self)
        #self.progressBar.setGeometry(QtCore.QRect(170, 290, 118, 23))
        # self.tab1_state.setObjectName("tab1_state")
        
        # Seperate line for buttons and pictures
        self.tab1_line = QtWidgets.QFrame(self.tab) # inhereit from tab
        #self.tab1_line.setGeometry(QtCore.QRect(0, 70, 461, 16))
        self.tab1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab1_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab1_line.setObjectName("tab1_line")

        # Button for performing the test
        self.tab1_test_button = QtWidgets.QPushButton(self.tab) # inhereit from tab
        #self.tab1_test_button.setGeometry(QtCore.QRect(370, 290, 75, 23))
        self.tab1_test_button.setMouseTracking(True)
        self.tab1_test_button.setObjectName("tab1_test_button")

        # Nesting layout
        self.tab1_vlayout = QtWidgets.QVBoxLayout(self.tab) # inhereit from tab. In order to line up widgets under self.tab???
        self.tab1_model_widget = QtWidgets.QWidget()
        self.tab1_model_widget_layout = QtWidgets.QHBoxLayout(self.tab1_model_widget) # inherit from tab. In order to line up widgets under tab1_model_widget???
        self.tab1_pic_path_widget = QtWidgets.QWidget()
        self.tab1_pic_path_widget_layout = QtWidgets.QHBoxLayout(self.tab1_pic_path_widget) # inherit from tab. In order to line up widgets under tab1_pic_path_widget???
        self.tab1_pic_widget = QtWidgets.QWidget()
        self.tab1_pic_widget_layout = QtWidgets.QHBoxLayout(self.tab1_pic_widget) # inherit from tab. In order to line up widgets under tab1_pic_widget???
        self.tab1_bottom_widget = QtWidgets.QWidget()
        self.tab1_bottom_widget_layout = QtWidgets.QHBoxLayout(self.tab1_bottom_widget) # inherit from tab. In order to line up widgets under tab1_bottom_widget???

        # add widget objects to layout object
        self.tab1_model_widget_layout.addWidget(self.tab1_model_button)
        self.tab1_model_widget_layout.addWidget(self.tab1_model_path)

        self.tab1_pic_path_widget_layout.addWidget(self.tab1_pic_button)
        self.tab1_pic_path_widget_layout.addWidget(self.tab1_pic_path)

        self.tab1_pic_widget_layout.addWidget(self.tab1_left_pic)
        self.tab1_pic_widget_layout.addWidget(self.tab1_right_pic)

        # self.tab1_bottom_widget_layout.addWidget(self.tab1_state)
        self.tab1_bottom_widget_layout.addWidget(self.tab1_test_button)

        self.tab1_vlayout.addWidget(self.tab1_model_widget, alignment=QtCore.Qt.AlignTop)
        self.tab1_vlayout.addWidget(self.tab1_pic_path_widget, alignment=QtCore.Qt.AlignTop)
        self.tab1_vlayout.addWidget(self.tab1_line, alignment=QtCore.Qt.AlignTop)
        self.tab1_vlayout.addWidget(self.tab1_pic_widget, alignment=QtCore.Qt.AlignTop)
        self.tab1_vlayout.addWidget(self.tab1_bottom_widget, alignment=QtCore.Qt.AlignBottom)
        
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
        self.tab2_left_pic = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.tab2_left_pic.setObjectName("tab2_left_pic")
        self.gridLayout_3.addWidget(self.tab2_left_pic, 0, 0, 1, 1)
        
        # Right grid for transformed picture
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 130, 201, 191))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tab2_right_pic = QtWidgets.QGraphicsView(self.gridLayoutWidget_4)
        self.tab2_right_pic.setObjectName("tab2_right_pic")
        self.gridLayout_4.addWidget(self.tab2_right_pic, 0, 0, 1, 1)
        
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
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Recognition"))
        self.tab1_pic_button.setText(_translate("MainWindow", "Select PIC"))
        self.tab1_model_button.setText(_translate("MainWindow", "Select Model"))
        self.tab1_test_button.setText(_translate("MainWindow", "Test!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Model Test Demo"))
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
        self.tab1_pic_button.clicked.connect(self.on_tab1_pic_button_Clicked)
        self.tab1_model_button.clicked.connect(self.on_tab1_model_button_Clicked)
        self.tab1_test_button.clicked.connect(self.on_tab1_test_button_Clicked)

        self.serialNumberCount = 0

    def tr(self, text):
        return QtCore.QObject.tr(self, text)

    def on_tab1_pic_button_Clicked(self):
        path_to_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, 
                self.tr("Load Image"), self.tr("~/Desktop/"), self.tr("Images (*.jpg)"))
        if path_to_file:
            self.tab1_pic_path.setText(path_to_file)
            left_pixmap = QtGui.QPixmap(path_to_file)
            left_pixmap = left_pixmap.scaled(550, 225, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            self.tab1_left_pic.setPixmap(left_pixmap)
            self.tab1_pic = path_to_file
        elif path_to_file == "":
            print("Nothing.")
            return
    
    def on_tab1_model_button_Clicked(self):
        path_to_file, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                self.tr("Load Model"), self.tr("~/Desktop/"), self.tr("Models (*.weights)"))
        if path_to_file:
            self.tab1_model_path.setText(path_to_file)
            self.tab1_model = path_to_file
        elif path_to_file == "":
            print("Nothing.")
            return

    def on_tab1_test_button_Clicked(self):
        if self.tab1_model == '':
            print("No model!")
            return
        elif self.tab1_pic == '':
            print("No Pic!")
            return
        
        darknetPath = 'github_repositories/VG_AlexeyAB_darknet/'
        # make directory to store detected samples and detection log
        detectionOutput = 'detection_output/'
        if os.path.isdir(detectionOutput) is False:
            os.mkdir(detectionOutput)
        
        # generate serial number
        date = datetime.now().strftime("%Y%m%d")
        serialNumber = date + '{0:03}'.format(self.serialNumberCount)
        while (os.path.isdir(detectionOutput + serialNumber) == False):
            self.serialNumberCount = self.serialNumberCount + 1
            serialNumber = date + '{0:03}'.format(self.serialNumberCount)
        
        detectionOutput = detectionOutput + serialNumber

        # create empty json file
        commands = ['touch',
                    detectionOutput + '/result.json']
        os.system(' '.join(commands))

        # movie = QtGui.QMovie('loading.gif')
        # movie.setCacheMode(QtGui.QMovie.CacheAll)
        # movie.setSpeed(100)
        # movie.setScaledSize(QtCore.QSize(50,50))
        # self.tab1_state.setMovie(movie)
        # movie.start()

        # run detection
        ### batch images detector (darknet) provided by vincentgong7 ###
        commands = ['./' + darknetPath + 'darknet detector batch',
                    darknetPath + 'data/obj.data',
                    darknetPath + 'cfg/yolov4-custom.cfg',
                    darknetPath + 'backup/20200509_20000iterations_random0_sub32_wh480/yolov4-custom_20000.weights',
                    'io_folder ' + self.tab1_pic,
                    detectionOutput,
                    '-out ' + detectionOutput + '/result.json',
                    '-dont_show -ext_output']
        os.system(' '.join(commands))

        img_path = "/home/mmnlab/Desktop/joey/20200430/darknet/predictions.jpg"
        right_pixmap = QtGui.QPixmap(img_path)
        right_pixmap = right_pixmap.scaled(550, 225, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_right_pic.setPixmap(right_pixmap)
        
        check = 'check.jpg'
        state_pixmap = QtGui.QPixmap(check)
        state_pixmap = state_pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.tab1_state.setPixmap(state_pixmap)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
