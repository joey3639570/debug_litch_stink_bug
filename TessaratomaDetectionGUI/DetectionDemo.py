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
        self.tabWidget.setStyleSheet("QTabBar::tab {height: 30px;}")
        self.tab1 = QtWidgets.QWidget() # declaration for tab, no inheritance needed
        self.tab1.setObjectName("tab1")

        # Instructions for orchard selecting
        self.tab1_orchard_instruction_label = QtWidgets.QLabel(self.tab1)
        self.tab1_orchard_instruction_label.setObjectName("tab1_orchard_instruction_label")
        self.tab1_orchard_instruction_label_font = QtGui.QFont()
        self.tab1_orchard_instruction_label_font.setPointSize(12)
        self.tab1_orchard_instruction_label.setFont(self.tab1_orchard_instruction_label_font)

        # ComboBox for orchard selecting
        self.tab1_orchard_comboBox = QtWidgets.QComboBox(self.tab1)
        self.tab1_orchard_comboBox.setObjectName('tab1_orchard_comboBox')
        
        # Instructions for picture selecting
        self.tab1_picture_path_instruction_label = QtWidgets.QLabel(self.tab1)
        self.tab1_picture_path_instruction_label.setObjectName("tab1_picture_path_instruction_label")
        self.tab1_picture_path_instruction_label.setFont(self.tab1_orchard_instruction_label_font) # reuse the font object to reduce the use of memory
        
        # Button for picture selecting
        self.tab1_picture_path_button = QtWidgets.QPushButton(self.tab1)  # parent is tab, which declares at line 26
        self.tab1_picture_path_button.setFixedWidth(140)
        self.tab1_picture_path_button.setMouseTracking(True)
        self.tab1_picture_path_button.setObjectName("tab1_picture_path_button")

        # Text for showing the path of the pic
        self.tab1_picture_path_lineEdit = QtWidgets.QLineEdit(self.tab1) # parent is tab
        self.tab1_picture_path_lineEdit.setObjectName("tab1_picture_path_lineEdit")
        self.tab1_picture_path = ''
        
        # Running state
        self.tab1_state_label = QtWidgets.QLabel(self.tab1)
        self.tab1_state_label.setObjectName("tab1_state_label")

        # Button for performing the test
        self.tab1_test_instruction_label = QtWidgets.QLabel(self.tab1)
        self.tab1_test_instruction_label.setObjectName("tab1_test_instruction_label")
        self.tab1_test_instruction_label.setFont(self.tab1_orchard_instruction_label_font)
        self.tab1_test_button = QtWidgets.QPushButton(self.tab1)  # parent is tab
        self.tab1_test_button.setMouseTracking(True)
        self.tab1_test_button.setObjectName("tab1_test_button")
        self.tab1_test_button.setEnabled(False)

        # Seperate line for buttons and pictures
        self.tab1_line = QtWidgets.QFrame(self.tab1) # parent is tab
        self.tab1_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tab1_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tab1_line.setObjectName("tab1_line")

        # Label for showing statistical data
        self.tab1_statistical_data_label_font = QtGui.QFont()
        self.tab1_statistical_data_label_font.setPointSize(12)
        self.tab1_statistical_data_date_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_date_label.setObjectName("tab1_statistical_data_time_label")
        self.tab1_statistical_data_dominant_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_dominant_label.setObjectName("tab1_statistical_data_dominant_label")
        self.tab1_statistical_data_dominant_label.setFont(self.tab1_statistical_data_label_font)

        self.tab1_statistical_data_egg_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_egg_label.setObjectName("tab1_statistical_data_egg_label")
        self.tab1_statistical_data_egg_label.setFont(self.tab1_statistical_data_label_font)
        self.tab1_statistical_data_egg_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab1_statistical_data_larval_before_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_larval_before_label.setObjectName("tab1_statistical_data_larval_before_label")
        self.tab1_statistical_data_larval_before_label.setFont(self.tab1_statistical_data_label_font)
        self.tab1_statistical_data_larval_before_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab1_statistical_data_larval_after_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_larval_after_label.setObjectName("tab1_statistical_data_larval_after_label")
        self.tab1_statistical_data_larval_after_label.setFont(self.tab1_statistical_data_label_font)
        self.tab1_statistical_data_larval_after_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab1_statistical_data_juvenile_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_juvenile_label.setObjectName("tab1_statistical_data_juvenile_label")
        self.tab1_statistical_data_juvenile_label.setFont(self.tab1_statistical_data_label_font)
        self.tab1_statistical_data_juvenile_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab1_statistical_data_tessaratoma_label = QtWidgets.QLabel(self.tab1)
        self.tab1_statistical_data_tessaratoma_label.setObjectName("tab1_statistical_data_tessaratoma_label")
        self.tab1_statistical_data_tessaratoma_label.setFont(self.tab1_statistical_data_label_font)
        self.tab1_statistical_data_tessaratoma_label.setAlignment(QtGui.Qt.AlignHCenter)

        # Left grid for original picture
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Button, brush)

        self.tab1_picture_navigate_button_font = QtGui.QFont()
        self.tab1_picture_navigate_button_font.setPointSize(14)

        self.tab1_left_picture = QtWidgets.QLabel(self.tab1)
        self.tab1_left_picture.setObjectName("tab1_left_picture")
        self.tab1_left_picture.setFixedWidth(560)
        self.tab1_left_picture.setFixedHeight(350)
        self.tab1_left_picture_navigate_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_left_picture_navigate_button.setEnabled(False)
        self.tab1_left_picture_navigate_button.setMouseTracking(True)
        self.tab1_left_picture_navigate_button.setFixedWidth(51)
        self.tab1_left_picture_navigate_button.setFixedHeight(350)
        self.tab1_left_picture_navigate_button.setObjectName("tab1_left_picture_navigate_button")
        self.tab1_left_picture_navigate_button.setPalette(palette)
        self.tab1_left_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font)
        
        # Right grid for detected picture
        self.tab1_right_picture = QtWidgets.QLabel(self.tab1)
        self.tab1_right_picture.setObjectName("tab1_right_picture")
        self.tab1_right_picture.setFixedWidth(560)
        self.tab1_right_picture.setFixedHeight(350)
        self.tab1_right_picture_navigate_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_right_picture_navigate_button.setEnabled(False)
        self.tab1_right_picture_navigate_button.setMouseTracking(True)
        self.tab1_right_picture_navigate_button.setFixedWidth(51)
        self.tab1_right_picture_navigate_button.setFixedHeight(350)
        self.tab1_right_picture_navigate_button.setObjectName("tab1_right_picture_navigate_button")
        self.tab1_right_picture_navigate_button.setPalette(palette)
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
        self.tab1_statistical_data_widget_layout = QtWidgets.QVBoxLayout(self.tab1_statistical_data_widget)
        self.tab1_statistical_data_objects_widget = QtWidgets.QWidget()
        self.tab1_statistical_data_objects_widget_layout = QtWidgets.QHBoxLayout(self.tab1_statistical_data_objects_widget)
        self.tab1_picture_widget = QtWidgets.QWidget()
        self.tab1_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab1_picture_widget) # parent is tab. In order to line up widgets under tab1_picture_widget???

        # orchard widget
        self.tab1_orchard_widget_layout.addWidget(self.tab1_orchard_comboBox)

        # picture path widget
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_path_button)
        self.tab1_picture_selection_widget_layout.addWidget(self.tab1_picture_path_lineEdit)

        # detection widget
        self.tab1_test_widget_layout.addWidget(self.tab1_test_button)

        # statistical data widget for objects
        self.tab1_statistical_data_objects_widget_layout.addWidget(self.tab1_statistical_data_egg_label)
        self.tab1_statistical_data_objects_widget_layout.addWidget(self.tab1_statistical_data_larval_before_label)
        self.tab1_statistical_data_objects_widget_layout.addWidget(self.tab1_statistical_data_larval_after_label)
        self.tab1_statistical_data_objects_widget_layout.addWidget(self.tab1_statistical_data_juvenile_label)
        self.tab1_statistical_data_objects_widget_layout.addWidget(self.tab1_statistical_data_tessaratoma_label)

        # statistical data widget
        self.tab1_statistical_data_widget_layout.addWidget(self.tab1_statistical_data_date_label)
        self.tab1_statistical_data_widget_layout.addWidget(self.tab1_statistical_data_dominant_label)
        self.tab1_statistical_data_widget_layout.addWidget(self.tab1_statistical_data_objects_widget)

        # pichture showing widget
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture_navigate_button)
        self.tab1_picture_widget_layout.addWidget(self.tab1_left_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture)
        self.tab1_picture_widget_layout.addWidget(self.tab1_right_picture_navigate_button)
        self.tab1_picture_widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # whole layout
        self.tab1_verticalLayout.addWidget(self.tab1_orchard_instruction_label)
        self.tab1_verticalLayout.addWidget(self.tab1_orchard_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_path_instruction_label)
        self.tab1_verticalLayout.addWidget(self.tab1_picture_selection_widget)
        self.tab1_verticalLayout.addWidget(self.tab1_test_instruction_label)
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
        
        # Instruction for orchard selecting
        self.tab2_orchard_instruction_label = QtWidgets.QLabel(self.tab2)
        self.tab2_orchard_instruction_label.setObjectName("tab2_orchard_instruction_label")
        self.tab2_orchard_instruction_label_font = QtGui.QFont()
        self.tab2_orchard_instruction_label_font.setPointSize(12)
        self.tab2_orchard_instruction_label.setFont(self.tab2_orchard_instruction_label_font)

        # ComboBox for orchard selecting
        self.tab2_orchard_comboBox = QtWidgets.QComboBox(self.tab2)
        self.tab2_orchard_comboBox.setObjectName('tab2_orchard_comboBox')

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
        self.tab2_dateAndOrchard_label = QtWidgets.QLabel(self.tab2)
        self.tab2_dateAndOrchard_label.setObjectName('tab2_date_label')
        self.tab2_dateAndOrchard_label.setAlignment(QtCore.Qt.AlignCenter)

        self.tab2_date_font = QtGui.QFont()
        self.tab2_date_font.setPointSize(12)
        self.tab2_dateAndOrchard_label.setFont(self.tab2_date_font)

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
        self.tab2_statistical_data_count_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_count_label.setObjectName("tab2_statistical_data_count_label")
        self.tab2_statistical_data_dominant_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_dominant_label.setObjectName("tab2_statistical_data_dominant_label")
        self.tab2_statistical_data_dominant_label.setFont(self.tab1_statistical_data_label_font) # reuse the font object to reduce the use of memory

        self.tab2_statistical_data_egg_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_egg_label.setObjectName("tab2_statistical_data_egg_label")
        self.tab2_statistical_data_egg_label.setFont(self.tab1_statistical_data_label_font) # reuse the font object to reduce the use of memory
        self.tab2_statistical_data_egg_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab2_statistical_data_larval_before_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_larval_before_label.setObjectName("tab2_statistical_data_larval_before_label")
        self.tab2_statistical_data_larval_before_label.setFont(self.tab1_statistical_data_label_font) # reuse the font object to reduce the use of memory
        self.tab2_statistical_data_larval_before_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab2_statistical_data_larval_after_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_larval_after_label.setObjectName("tab2_statistical_data_larval_after_label")
        self.tab2_statistical_data_larval_after_label.setFont(self.tab1_statistical_data_label_font) # reuse the font object to reduce the use of memory
        self.tab2_statistical_data_larval_after_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab2_statistical_data_juvenile_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_juvenile_label.setObjectName("tab2_statistical_data_juvenile_label")
        self.tab2_statistical_data_juvenile_label.setFont(self.tab1_statistical_data_label_font) # reuse the font object to reduce the use of memory
        self.tab2_statistical_data_juvenile_label.setAlignment(QtGui.Qt.AlignHCenter)
        self.tab2_statistical_data_tessaratoma_label = QtWidgets.QLabel(self.tab2)
        self.tab2_statistical_data_tessaratoma_label.setObjectName("tab2_statistical_data_tessaratoma_label")
        self.tab2_statistical_data_tessaratoma_label.setFont(self.tab1_statistical_data_label_font) # reuse the font object to reduce the use of memory
        self.tab2_statistical_data_tessaratoma_label.setAlignment(QtGui.Qt.AlignHCenter)

        # Left grid for original picture
        self.tab2_left_picture = QtWidgets.QLabel(self.tab2)
        self.tab2_left_picture.setObjectName("tab2_left_picture")
        self.tab2_left_picture.setFixedWidth(560)
        self.tab2_left_picture.setFixedHeight(420)
        self.tab2_left_picture_navigate_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_left_picture_navigate_button.setEnabled(False)
        self.tab2_left_picture_navigate_button.setMouseTracking(True)
        self.tab2_left_picture_navigate_button.setFixedWidth(51)
        self.tab2_left_picture_navigate_button.setFixedHeight(420)
        self.tab2_left_picture_navigate_button.setObjectName("tab2_left_picture_navigate_button")
        self.tab2_left_picture_navigate_button.setPalette(palette)
        
        # Right grid for detected picture
        self.tab2_right_picture = QtWidgets.QLabel(self.tab2)
        self.tab2_right_picture.setObjectName("tab2_right_picture")
        self.tab2_right_picture.setFixedWidth(560)
        self.tab2_right_picture.setFixedHeight(420)
        self.tab2_right_picture_navigate_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_right_picture_navigate_button.setEnabled(False)
        self.tab2_right_picture_navigate_button.setMouseTracking(True)
        self.tab2_right_picture_navigate_button.setFixedWidth(51)
        self.tab2_right_picture_navigate_button.setFixedHeight(420)
        self.tab2_right_picture_navigate_button.setObjectName("tab2_right_picture_navigate_button")
        self.tab2_right_picture_navigate_button.setPalette(palette)

        self.tab2_left_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font) # reuse the font object to reduce the use of memory
        self.tab2_right_picture_navigate_button.setFont(self.tab1_picture_navigate_button_font) # reuse the font object to reduce the use of memory

        # nesting layout
        self.tab2_verticalLayout = QtWidgets.QVBoxLayout(self.tab2)  # parent is tab. In order to line up widgets under self.tab2???
        self.tab2_orchard_widget = QtWidgets.QWidget()
        self.tab2_orchard_widget_layout = QtWidgets.QVBoxLayout(self.tab2_orchard_widget)
        self.tab2_date_selection_widget = QtWidgets.QWidget()
        self.tab2_date_selection_widget_layout = QtWidgets.QHBoxLayout(self.tab2_date_selection_widget)
        self.tab2_statistical_data_widget = QtWidgets.QWidget()
        self.tab2_statistical_data_widget_layout = QtWidgets.QVBoxLayout(self.tab2_statistical_data_widget)
        self.tab2_statistical_data_objects_widget = QtWidgets.QWidget()
        self.tab2_statistical_data_objects_widget_layout = QtWidgets.QHBoxLayout(self.tab2_statistical_data_objects_widget)
        self.tab2_picture_widget = QtWidgets.QWidget()
        self.tab2_picture_widget_layout = QtWidgets.QHBoxLayout(self.tab2_picture_widget)

        # orchard comboBox and running state
        self.tab2_orchard_widget_layout.addWidget(self.tab2_orchard_comboBox)

        # date selection widget
        self.tab2_date_selection_widget_layout.addWidget(self.tab2_left_date_navigate_button)
        self.tab2_date_selection_widget_layout.addWidget(self.tab2_dateAndOrchard_label)
        self.tab2_date_selection_widget_layout.addWidget(self.tab2_right_date_navigate_button)

        # picture showing widget
        self.tab2_picture_widget_layout.addWidget(self.tab2_left_picture_navigate_button)
        self.tab2_picture_widget_layout.addWidget(self.tab2_left_picture)
        self.tab2_picture_widget_layout.addWidget(self.tab2_right_picture)
        self.tab2_picture_widget_layout.addWidget(self.tab2_right_picture_navigate_button)
        self.tab2_picture_widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        # statistical data widget for objects
        self.tab2_statistical_data_objects_widget_layout.addWidget(self.tab2_statistical_data_egg_label)
        self.tab2_statistical_data_objects_widget_layout.addWidget(self.tab2_statistical_data_larval_before_label)
        self.tab2_statistical_data_objects_widget_layout.addWidget(self.tab2_statistical_data_larval_after_label)
        self.tab2_statistical_data_objects_widget_layout.addWidget(self.tab2_statistical_data_juvenile_label)
        self.tab2_statistical_data_objects_widget_layout.addWidget(self.tab2_statistical_data_tessaratoma_label)

        # statistical data widget
        self.tab2_statistical_data_widget_layout.addWidget(self.tab2_statistical_data_count_label)
        self.tab2_statistical_data_widget_layout.addWidget(self.tab2_statistical_data_dominant_label)
        self.tab2_statistical_data_widget_layout.addWidget(self.tab2_statistical_data_objects_widget)

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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate('MainWindow', 'Tessaratoma Detection'))

        # tab 1
        self.tab1_orchard_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '1. Select orchard'))
        self.tab1_orchard_instruction_label.setStyleSheet("color: rgb(0, 146, 208);")
        self.tab1_orchard_comboBox.setPlaceholderText(QtCore.QCoreApplication.translate('MainWindow', '--Select orchard--'))
        self.tab1_orchard_comboBox.addItem(QtCore.QCoreApplication.translate('MainWindow', 'Orchard 1')) # hard coded for demo
        self.tab1_orchard_comboBox.addItem(QtCore.QCoreApplication.translate('MainWindow', 'Orchard 2'))
        self.tab1_orchard_comboBox.addItem(QtCore.QCoreApplication.translate('MainWindow', 'Orchard 3'))
        self.tab1_orchard_comboBox.setCurrentIndex(-1)
        self.tab1_picture_path_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '2. Click \"Browse\" to select the directory containing the pictures to detect'))
        self.tab1_picture_path_button.setText(QtCore.QCoreApplication.translate('MainWindow', 'Browse'))
        self.tab1_test_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '3. Click \"DETECT\" to start detecting bugs'))
        self.tab1_test_button.setText(QtCore.QCoreApplication.translate('MainWindow', 'DETECT'))
        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
        self.tab1_left_picture_navigate_button.setText(QtCore.QCoreApplication.translate('MainWindow', '<'))
        self.tab1_right_picture_navigate_button.setText(QtCore.QCoreApplication.translate('MainWindow', '>'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtCore.QCoreApplication.translate('MainWindow', 'Detection'))
        
        # tab 2
        self.tab2_orchard_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '1. Select orchard'))
        self.tab2_orchard_instruction_label.setStyleSheet("color: rgb(0, 146, 208);")
        self.tab2_orchard_comboBox.setPlaceholderText(QtCore.QCoreApplication.translate('MainWindow', '--Select orchard--'))
        self.tab2_orchard_comboBox.addItem(QtCore.QCoreApplication.translate('MainWindow', 'Orchard 1')) # hard coded for demo
        self.tab2_orchard_comboBox.addItem(QtCore.QCoreApplication.translate('MainWindow', 'Orchard 2'))
        self.tab2_orchard_comboBox.addItem(QtCore.QCoreApplication.translate('MainWindow', 'Orchard 3'))
        self.tab2_orchard_comboBox.setCurrentIndex(-1)
        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
        self.tab2_date_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '2. Select the date'))
        self.tab2_left_date_navigate_button.setText(QtCore.QCoreApplication.translate('MainWindow', '<'))
        self.tab2_right_date_navigate_button.setText(QtCore.QCoreApplication.translate('MainWindow', '>'))
        self.tab2_left_picture_navigate_button.setText(QtCore.QCoreApplication.translate('MainWindow', '<'))
        self.tab2_right_picture_navigate_button.setText(QtCore.QCoreApplication.translate('MainWindow', '>'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QtCore.QCoreApplication.translate('MainWindow', 'Statistical data'))


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
        self.tab2_dateNavigateCount = 0
        
        self.tab2_originalPictureDirectoryPath = ''
        self.tab2_originalPictureAddresses = []
        self.tab2_pictureNavigateCount = 0

        # Signal Setting
        # tab bar
        self.tabWidget.currentChanged['int'].connect(self.on_tabWidget_changed)

        # tab1
        self.tab1_orchard_comboBox.currentIndexChanged.connect(self.on_tab1_orchard_comboBox_changed)
        self.tab1_picture_path_button.clicked.connect(self.on_tab1_picture_button_clicked)
        self.tab1_test_button.clicked.connect(self.on_tab1_test_button_clicked)
        self.tab1_left_picture_navigate_button.clicked.connect(self.on_tab1_left_picutre_navigate_button_clicked)
        self.tab1_right_picture_navigate_button.clicked.connect(self.on_tab1_right_picutre_navigate_button_clicked)
        
        # tab2
        self.tab2_orchard_comboBox.currentIndexChanged.connect(self.on_tab2_orchard_comboBox_changed)
        self.tab2_left_picture_navigate_button.clicked.connect(self.on_tab2_left_picutre_navigate_button_clicked)
        self.tab2_right_picture_navigate_button.clicked.connect(self.on_tab2_right_picutre_navigate_button_clicked)
        self.tab2_left_date_navigate_button.clicked.connect(self.on_tab2_left_date_navigate_button_clicked)
        self.tab2_right_date_navigate_button.clicked.connect(self.on_tab2_right_date_navigate_button_clicked)

        # variables for line edit style
        self.lineEditOriginalStyle = self.tab1_picture_path_lineEdit.styleSheet()

    
    # generic functions
    def update_pictures(self, leftPictureAddress, rightPictureAddress, leftPicture, rightPicture, width, height):
        leftPixmap = QtGui.QPixmap(leftPictureAddress)
        leftPixmap = leftPixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        leftPicture.setAlignment(QtCore.Qt.AlignCenter)
        leftPicture.setPixmap(leftPixmap)
        rightPixmap = QtGui.QPixmap(rightPictureAddress)
        rightPixmap = rightPixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        rightPicture.setAlignment(QtCore.Qt.AlignCenter)
        rightPicture.setPixmap(rightPixmap)

        return
    

    def collect_original_picutre_addresses(self, detectedDirectory, originalPictureAddresses):
        for f in os.listdir(detectedDirectory):
            if (f.lower().__contains__('.jpg')):
                originalPictureAddresses.append(detectedDirectory + f)
            elif (f.lower().__contains__('.jpeg')):
                originalPictureAddresses.append(detectedDirectory + f)
            elif (f.lower().__contains__('.png')):
                originalPictureAddresses.append(detectedDirectory + f)
        
        originalPictureAddresses.sort()

        return


    # functions for tabWidget
    def on_tabWidget_changed(self, index):
        if index == 1 and self.tab2_orchard_comboBox.currentIndex() != -1:  # "statistical data" tab
            self.on_tab2_orchard_comboBox_changed()
        return

    
    def on_tab1_orchard_comboBox_changed(self):
        self.tab1_orchard_instruction_label.setStyleSheet("color: black;")
        if self.tab1_picture_path_lineEdit.text() == '':
            self.tab1_picture_path_instruction_label.setStyleSheet("color: rgb(0, 146, 208);")
        else:
            self.tab1_test_button.setEnabled(True)
        return


    # functions for tab1
    def on_tab1_picture_button_clicked(self):
        # dialog for selecting directory
        path = QtWidgets.QFileDialog.getExistingDirectory(self, QtCore.QCoreApplication.translate('MainWindow', 'Select directory'), '/home/mmnlab/')

        if path:
            # update picture path when a directory is selected
            self.tab1_picture_path_lineEdit.setText(path)
            self.tab1_picture_path = path + '/'
            self.tab1_picture_path_lineEdit.setStyleSheet(self.lineEditOriginalStyle)
            
            if len(os.listdir(path)) == 0:
                # show some prompts when the selected directory is empty
                self.tab1_picture_path_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '2. The directory is empty. Please select another one'))
                self.tab1_picture_path_instruction_label.setStyleSheet("color: red;")
                self.tab1_picture_path_lineEdit.setStyleSheet("border: 1px solid red;")
                self.tab1_test_button.setEnabled(False)
            else:
                # remove the prompts
                self.tab1_picture_path_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '2. Click \"Browse\" to select the directory containing the pictures to detect'))
                self.tab1_picture_path_instruction_label.setStyleSheet("color: black;")
                self.tab1_picture_path_lineEdit.setStyleSheet(self.lineEditOriginalStyle)
                # check the state of the comboBox for orchard selecting
                if self.tab1_orchard_comboBox.currentIndex() == -1:
                    # show some prompts when orchard is not selected
                    self.tab1_orchard_instruction_label.setStyleSheet("color: red;")
                    self.tab1_test_button.setEnabled(False)
                else:
                    # remove the prompts for orchard selecting
                    self.tab1_orchard_instruction_label.setStyleSheet("color: black;")
                    self.tab1_test_instruction_label.setStyleSheet("color: rgb(0, 146, 208);")
                    self.tab1_test_button.setEnabled(True)

            self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Selected directory: ') + path)
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        elif path == '':
            # show some prompts when no directory is selected
            if self.tab1_picture_path_lineEdit.text() == '':
                self.tab1_picture_path_instruction_label.setText(QtCore.QCoreApplication.translate('MainWindow', '2. No directory selected. Please select a directory to start detecting bugs'))
                self.tab1_picture_path_instruction_label.setStyleSheet("color: red;")
                self.tab1_picture_path_lineEdit.setStyleSheet("border: 1px solid red;")

                self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'No directory selected. Please select a directory to start detecting bugs'))
                QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return


    def on_tab1_test_button_clicked(self):
        # remove prompt
        self.tab1_test_instruction_label.setStyleSheet("color: black;")
        
        # remove old information
        self.tab1_statistical_data_date_label.clear()
        self.tab1_statistical_data_dominant_label.clear()
        self.tab1_statistical_data_egg_label.clear()
        self.tab1_statistical_data_larval_before_label.clear()
        self.tab1_statistical_data_larval_after_label.clear()
        self.tab1_statistical_data_juvenile_label.clear()
        self.tab1_statistical_data_tessaratoma_label.clear()
        self.tab1_left_picture.clear()
        self.tab1_right_picture.clear()

        # disable buttons
        self.tab1_orchard_comboBox.setEnabled(False)
        self.tab1_picture_path_button.setEnabled(False)
        self.tab1_picture_path_lineEdit.setEnabled(False)
        self.tab1_test_button.setEnabled(False)
        self.tab1_left_picture_navigate_button.setEnabled(False)
        self.tab1_right_picture_navigate_button.setEnabled(False)
        
        # initialize variables
        self.tab1_pictureNavigateCount = 0
        self.tab1_originalPictureAddresses = []

        self.tab1_originalPictureDirectoryPath = self.tab1_picture_path

        # create directory to store detected samples and detection log
        self.tab1_detectionOutputPath = os.path.abspath('.') + '/detection_output/'
        if os.path.isdir(self.tab1_detectionOutputPath) is False:
            os.mkdir(self.tab1_detectionOutputPath)
            self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Directory: ') + self.tab1_detectionOutputPath + \
                                            QtCore.QCoreApplication.translate('MainWindow', ' created'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        else:
            self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Directory: ') + self.tab1_detectionOutputPath + \
                                            QtCore.QCoreApplication.translate('MainWindow', ' already existed'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        resultDirectoryName = str(self.tab1_orchard_comboBox.currentIndex() + 1) + '_' + date.replace('/', '').replace(':', '').replace(' ', '_')
        self.tab1_detectionOutputPath = self.tab1_detectionOutputPath + resultDirectoryName + '/'
        os.mkdir(self.tab1_detectionOutputPath)

        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Directory: ') + self.tab1_detectionOutputPath + \
                                        QtCore.QCoreApplication.translate('MainWindow', ' created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # create empty detection log file
        commands = ['touch',
                    self.tab1_detectionOutputPath + 'detection_results.json']
        os.system(' '.join(commands))

        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Detection log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        # create empty statistics log file
        commands = ['touch',
                    self.tab1_detectionOutputPath + 'statistics.json']
        os.system(' '.join(commands))

        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Statistics log file created'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # run the detection
        ### batch images detector (darknet) provided by vincentgong7 ###
        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Detection started, please wait...'))
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
        
        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Detection finished'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # collecting paths to all the pictures for detection
        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Collecting paths'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        self.collect_original_picutre_addresses(self.tab1_originalPictureDirectoryPath, self.tab1_originalPictureAddresses)

        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Paths collected'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # statistical data
        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Generating statistical data'))
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

        detectedObjectTotal = sum(detectedObjectCount)
        dominantObject = 0
        dominantObjectName = ''
        for i in range(1, len(detectedObjectCount)):
            if detectedObjectCount[dominantObject] < detectedObjectCount[i]:
                dominantObject = i
        
        if dominantObject == 0:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow', 'egg')
        elif dominantObject == 1:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','larval_before')
        elif dominantObject == 2:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','larval_after')
        elif dominantObject == 3:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','juvenile')
        elif dominantObject == 4:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','tessaratoma')

        statisticsDictionary = {
            "time": date,
            "orchard": (self.tab1_orchard_comboBox.currentIndex() + 1), 
            "detection_result_path": self.tab1_detectionOutputPath + 'detection_results.json',
            "detected_directory": self.tab1_originalPictureDirectoryPath,
            "dominant_object": dominantObject,
            "objects_count": {"egg": detectedObjectCount[0], "larval_before": detectedObjectCount[1], "larval_after": detectedObjectCount[2], "juvenile": detectedObjectCount[3], "tessaratoma": detectedObjectCount[4]}
        }

        with open(self.tab1_detectionOutputPath + 'statistics.json', 'w') as outfile:
            outfile.write(json.dumps(statisticsDictionary, indent=4))
        
        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Statistical data saved successfully'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        # show pictures
        self.update_pictures(self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount],
                            self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount].replace(self.tab1_originalPictureDirectoryPath, self.tab1_detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab1_left_picture, self.tab1_right_picture,
                            560, 350)

        # show statistical data in main window
        self.tab1_statistical_data_date_label.setText(date + QtCore.QCoreApplication.translate('MainWindow', ' , at ') + self.tab1_orchard_comboBox.currentText() + \
                                                        QtCore.QCoreApplication.translate('MainWindow', ' . ') + str(len(self.tab1_originalPictureAddresses)) + \
                                                        QtCore.QCoreApplication.translate('MainWindow', ' pictures , ') + str(detectedObjectTotal) + \
                                                        QtCore.QCoreApplication.translate('MainWindow', ' bugs.'))
        
        self.tab1_statistical_data_dominant_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'DOMINANT OBJECT: ') + dominantObjectName)
        
        self.tab1_statistical_data_egg_label.setStyleSheet("background-color: rgb(255, 191, 255);")
        self.tab1_statistical_data_egg_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'egg: ') + str(detectedObjectCount[0]) + ' (' + \
                                                        str(round(detectedObjectCount[0]/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab1_statistical_data_larval_before_label.setStyleSheet("background-color: rgb(255, 255, 149);")
        self.tab1_statistical_data_larval_before_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'larval_before: ') + str(detectedObjectCount[1]) + ' (' + \
                                                                str(round(detectedObjectCount[1]/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab1_statistical_data_larval_after_label.setStyleSheet("background-color: rgb(191, 255, 255);")
        self.tab1_statistical_data_larval_after_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'larval_after: ') + str(detectedObjectCount[2]) + ' (' + \
                                                                str(round(detectedObjectCount[2]/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab1_statistical_data_juvenile_label.setStyleSheet("background-color: rgb(255, 191, 191);")
        self.tab1_statistical_data_juvenile_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'juvenile: ') + str(detectedObjectCount[3]) + ' (' + \
                                                            str(round(detectedObjectCount[3]/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab1_statistical_data_tessaratoma_label.setStyleSheet("background-color: rgb(191, 255, 191);")
        self.tab1_statistical_data_tessaratoma_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'tessaratoma: ') + str(detectedObjectCount[4]) + ' (' + \
                                                                str(round(detectedObjectCount[4]/detectedObjectTotal*100, 1)) + '%)')

        # show statistical data in message box
        statisticalDataMessage = QtWidgets.QMessageBox()
        statisticalDataMessage.setWindowTitle(QtCore.QCoreApplication.translate('MainWindow', 'Statistical result'))
        statisticalDataMessage.setInformativeText(date + QtCore.QCoreApplication.translate('MainWindow', ' , at ') + self.tab1_orchard_comboBox.currentText() + '\n' + \
                                                    QtCore.QCoreApplication.translate('MainWindow', 'DOMINANT OBJECT: ') + dominantObjectName + '\n' + \
                                                    '    ' + QtCore.QCoreApplication.translate('MainWindow', 'egg: ') + str(detectedObjectCount[0]) + ' (' + \
                                                            str(round(detectedObjectCount[0]/detectedObjectTotal*100, 1)) + '%)\n' + \
                                                    '    ' + QtCore.QCoreApplication.translate('MainWindow', 'larval_before: ') + str(detectedObjectCount[1]) + ' (' + \
                                                            str(round(detectedObjectCount[1]/detectedObjectTotal*100, 1)) + '%)\n' + \
                                                    '    ' + QtCore.QCoreApplication.translate('MainWindow', 'larval_after: ') + str(detectedObjectCount[2]) + ' (' + \
                                                            str(round(detectedObjectCount[2]/detectedObjectTotal*100, 1)) + '%)\n' + \
                                                    '    ' + QtCore.QCoreApplication.translate('MainWindow', 'juvenile: ') + str(detectedObjectCount[3]) + ' (' + \
                                                            str(round(detectedObjectCount[3]/detectedObjectTotal*100, 1)) + '%)\n' + \
                                                    '    ' + QtCore.QCoreApplication.translate('MainWindow', 'tessaratoma: ') + str(detectedObjectCount[4]) + ' (' + \
                                                            str(round(detectedObjectCount[4]/detectedObjectTotal*100, 1)) + '%)\n')
        
        statisticalDataMessage.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        statisticalDataMessage.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
        statisticalDataMessage.exec()

        # re-enable buttons
        self.tab1_orchard_comboBox.setEnabled(True)
        self.tab1_picture_path_button.setEnabled(True)
        self.tab1_picture_path_lineEdit.setEnabled(True)
        self.tab1_test_button.setEnabled(True)
        if len(self.tab1_originalPictureAddresses) > 1:
            self.tab1_right_picture_navigate_button.setEnabled(True)

        self.tab1_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        return


    def on_tab1_left_picutre_navigate_button_clicked(self):
        self.tab1_pictureNavigateCount = self.tab1_pictureNavigateCount - 1
        
        self.update_pictures(self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount],
                            self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount].replace(self.tab1_originalPictureDirectoryPath, self.tab1_detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab1_left_picture, self.tab1_right_picture,
                            560, 350)
        
        # control buttons
        if self.tab1_pictureNavigateCount == 0:
            self.tab1_left_picture_navigate_button.setEnabled(False)
        
        if self.tab1_right_picture_navigate_button.isEnabled() == False:
            self.tab1_right_picture_navigate_button.setEnabled(True)
        
        return
            

    def on_tab1_right_picutre_navigate_button_clicked(self):
        self.tab1_pictureNavigateCount = self.tab1_pictureNavigateCount + 1

        self.update_pictures(self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount],
                            self.tab1_originalPictureAddresses[self.tab1_pictureNavigateCount].replace(self.tab1_originalPictureDirectoryPath, self.tab1_detectionOutputPath).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab1_left_picture, self.tab1_right_picture,
                            560, 350)
        
        # control buttons
        if self.tab1_pictureNavigateCount == len(self.tab1_originalPictureAddresses) - 1:
            self.tab1_right_picture_navigate_button.setEnabled(False)
        
        if self.tab1_left_picture_navigate_button.isEnabled() == False:
            self.tab1_left_picture_navigate_button.setEnabled(True)
                
        return

    
    def on_tab2_orchard_comboBox_changed(self):
        # remove old information
        self.tab2_dateAndOrchard_label.clear()
        self.tab2_statistical_data_count_label.clear()
        self.tab2_statistical_data_dominant_label.clear()
        self.tab2_statistical_data_egg_label.clear()
        self.tab2_statistical_data_larval_before_label.clear()
        self.tab2_statistical_data_larval_after_label.clear()
        self.tab2_statistical_data_juvenile_label.clear()
        self.tab2_statistical_data_tessaratoma_label.clear()
        self.tab2_left_picture.clear()
        self.tab2_right_picture.clear()

        # disable buttons
        self.tab2_orchard_comboBox.setEnabled(False)
        self.tab2_left_picture_navigate_button.setEnabled(False)
        self.tab2_right_picture_navigate_button.setEnabled(False)
        self.tab2_left_date_navigate_button.setEnabled(False)
        self.tab2_right_date_navigate_button.setEnabled(False)
        
        # initialize variables
        self.tab2_dateNavigateCount = 0
        self.tab2_pictureNavigateCount = 0
        self.tab2_detectionOutputPaths = []
        self.tab2_originalPictureAddresses = []
        self.tab2_orchard_instruction_label.setStyleSheet("color: black;")

        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        # collect detection records of selected orchard
        collect_output_paths_return = self.tab2_collect_output_paths_of_selected_orchard()

        # 1: "detection_output" directory does not exist, 2: there isn't any detection records for selected orchard
        if collect_output_paths_return == 1:
            self.tab2_orchard_comboBox.setEnabled(True)
            self.tab2_dateAndOrchard_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'No data to show'))
            self.tab2_statistical_data_dominant_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'No data to show'))
            self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
            QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
            return

        # read the statistics.json
        f = open(self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount] + 'statistics.json')
        openedStatisticalData = json.load(f)
        f.close()

        self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']

        self.collect_original_picutre_addresses(self.tab2_originalPictureDirectoryPath, self.tab2_originalPictureAddresses)
        self.tab2_update_statistical_data(openedStatisticalData)
        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture, self.tab2_right_picture,
                            560, 420)

        # re-enable buttons
        self.tab2_orchard_comboBox.setEnabled(True)
        if len(self.tab2_detectionOutputPaths) > 1:
                self.tab2_right_date_navigate_button.setEnabled(True)
            
        if len(self.tab2_originalPictureAddresses) > 1:
            self.tab2_right_picture_navigate_button.setEnabled(True)
    
        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return
    

    def on_tab2_left_date_navigate_button_clicked(self):
        self.tab2_left_picture_navigate_button.setEnabled(False)
        self.tab2_right_picture_navigate_button.setEnabled(False)
        self.tab2_pictureNavigateCount = 0
        self.tab2_originalPictureAddresses = []

        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        self.tab2_dateNavigateCount = self.tab2_dateNavigateCount - 1

        # read the statistics.json
        f = open(self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount] + 'statistics.json')
        openedStatisticalData = json.load(f)
        f.close()

        self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']

        self.collect_original_picutre_addresses(self.tab2_originalPictureDirectoryPath, self.tab2_originalPictureAddresses)
        self.tab2_update_statistical_data(openedStatisticalData)
        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture, self.tab2_right_picture,
                            560, 420)

        # control buttons
        if self.tab2_dateNavigateCount == 0:
            self.tab2_left_date_navigate_button.setEnabled(False)
        
        if self.tab2_right_date_navigate_button.isEnabled() == False:
            self.tab2_right_date_navigate_button.setEnabled(True)
        
        if len(self.tab2_originalPictureAddresses) > 1:
                self.tab2_right_picture_navigate_button.setEnabled(True)

        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return
    

    def on_tab2_right_date_navigate_button_clicked(self):
        self.tab2_left_picture_navigate_button.setEnabled(False)
        self.tab2_right_picture_navigate_button.setEnabled(False)
        self.tab2_pictureNavigateCount = 0
        self.tab2_originalPictureAddresses = []

        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Loading. Please wait...'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)

        self.tab2_dateNavigateCount = self.tab2_dateNavigateCount + 1

        # read the statistics.json
        f = open(self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount] + 'statistics.json')
        openedStatisticalData = json.load(f)
        f.close()

        self.tab2_originalPictureDirectoryPath = openedStatisticalData['detected_directory']

        self.collect_original_picutre_addresses(self.tab2_originalPictureDirectoryPath, self.tab2_originalPictureAddresses)
        self.tab2_update_statistical_data(openedStatisticalData)
        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture, self.tab2_right_picture,
                            560, 420)

        # control buttons
        if self.tab2_dateNavigateCount == len(self.tab2_detectionOutputPaths) - 1:
            self.tab2_right_date_navigate_button.setEnabled(False)
        
        if self.tab2_left_date_navigate_button.isEnabled() == False:
            self.tab2_left_date_navigate_button.setEnabled(True)

        if len(self.tab2_originalPictureAddresses) > 1:
                self.tab2_right_picture_navigate_button.setEnabled(True)

        self.tab2_state_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'Ready'))
        QtCore.QCoreApplication.processEvents(QtCore.QEventLoop.AllEvents)
        
        return

    
    def on_tab2_left_picutre_navigate_button_clicked(self):
        self.tab2_pictureNavigateCount = self.tab2_pictureNavigateCount - 1
        
        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture, self.tab2_right_picture,
                            560, 420)
        
        # control buttons
        if self.tab2_pictureNavigateCount == 0:
            self.tab2_left_picture_navigate_button.setEnabled(False)
        
        if self.tab2_right_picture_navigate_button.isEnabled() == False:
            self.tab2_right_picture_navigate_button.setEnabled(True)
        
        return
            

    def on_tab2_right_picutre_navigate_button_clicked(self):
        self.tab2_pictureNavigateCount = self.tab2_pictureNavigateCount + 1

        self.update_pictures(self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount],
                            self.tab2_originalPictureAddresses[self.tab2_pictureNavigateCount].replace(self.tab2_originalPictureDirectoryPath, self.tab2_detectionOutputPaths[self.tab2_dateNavigateCount]).replace('.jpeg', '.jpg').replace('.png', '.jpg'),
                            self.tab2_left_picture, self.tab2_right_picture,
                            560, 420)
        
        # control buttons
        if self.tab2_pictureNavigateCount == len(self.tab2_originalPictureAddresses) - 1:
            self.tab2_right_picture_navigate_button.setEnabled(False)
        
        if self.tab2_left_picture_navigate_button.isEnabled() == False:
            self.tab2_left_picture_navigate_button.setEnabled(True)
                
        return

    
    def tab2_update_statistical_data(self, openedStatisticalData):
        dominantObjectName = ''
        
        detectedObjectTotal = openedStatisticalData['objects_count']['egg'] + openedStatisticalData['objects_count']['larval_before'] + openedStatisticalData['objects_count']['larval_after'] + \
                                openedStatisticalData['objects_count']['juvenile'] + openedStatisticalData['objects_count']['tessaratoma']
        
        if openedStatisticalData['dominant_object'] == 0:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow', 'egg')
        elif openedStatisticalData['dominant_object'] == 1:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','larval_before')
        elif openedStatisticalData['dominant_object'] == 2:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','larval_after')
        elif openedStatisticalData['dominant_object'] == 3:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow','juvenile')
        elif openedStatisticalData['dominant_object'] == 4:
            dominantObjectName = QtCore.QCoreApplication.translate('MainWindow', 'tessaratoma')
        
        # update the information shown on the main window
        self.tab2_dateAndOrchard_label.setText(openedStatisticalData['time'] + QtCore.QCoreApplication.translate('MainWindow', ' , at ') + QtCore.QCoreApplication.translate('MainWindow', 'Orchard ') + \
                                                str(openedStatisticalData['orchard']))

        self.tab2_statistical_data_count_label.setText(str(len(self.tab2_originalPictureAddresses)) + QtCore.QCoreApplication.translate('MainWindow', ' pictures , ') + \
                                                        str(detectedObjectTotal) + QtCore.QCoreApplication.translate('MainWindow', ' bugs.'))

        self.tab2_statistical_data_dominant_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'DOMINANT OBJECT: ') + dominantObjectName)
        
        self.tab2_statistical_data_egg_label.setStyleSheet("background-color: rgb(255, 191, 255);")
        self.tab2_statistical_data_egg_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'egg: ') + str(openedStatisticalData['objects_count']['egg']) + ' (' + \
                                                        str(round(int(openedStatisticalData['objects_count']['egg']) / detectedObjectTotal * 100, 1)) + '%)')
        
        self.tab2_statistical_data_larval_before_label.setStyleSheet("background-color: rgb(255, 255, 149);")
        self.tab2_statistical_data_larval_before_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'larval_before: ') + str(openedStatisticalData['objects_count']['larval_before']) + ' (' + \
                                                                str(round(int(openedStatisticalData['objects_count']['larval_before'])/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab2_statistical_data_larval_after_label.setStyleSheet("background-color: rgb(191, 255, 255);")
        self.tab2_statistical_data_larval_after_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'larval_after: ') + str(openedStatisticalData['objects_count']['larval_after']) + ' (' + \
                                                                str(round(int(openedStatisticalData['objects_count']['larval_after'])/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab2_statistical_data_juvenile_label.setStyleSheet("background-color: rgb(255, 191, 191);")
        self.tab2_statistical_data_juvenile_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'juvenile: ') + str(openedStatisticalData['objects_count']['juvenile']) + ' (' + \
                                                            str(round(int(openedStatisticalData['objects_count']['juvenile'])/detectedObjectTotal*100, 1)) + '%)')
        
        self.tab2_statistical_data_tessaratoma_label.setStyleSheet("background-color: rgb(191, 255, 191);")
        self.tab2_statistical_data_tessaratoma_label.setText(QtCore.QCoreApplication.translate('MainWindow', 'tessaratoma: ') + str(openedStatisticalData['objects_count']['tessaratoma']) + ' (' + \
                                                            str(round(int(openedStatisticalData['objects_count']['tessaratoma'])/detectedObjectTotal*100, 1)) + '%)')
        
        return
    

    def tab2_collect_output_paths_of_selected_orchard(self):
        orchardNumber = str(self.tab2_orchard_comboBox.currentIndex() + 1)
        detectionOutputDirectory = os.path.abspath('.') + '/detection_output'
        
        # return 1 if the directory "detection_output" doesn't exist
        if os.path.exists(detectionOutputDirectory) is False:
            return 1
        
        for p in os.listdir(os.path.abspath('.') + '/detection_output'):
            if (p[0] == orchardNumber and os.path.exists(detectionOutputDirectory + '/' + p + '/statistics.json')):
                self.tab2_detectionOutputPaths.append(detectionOutputDirectory + '/' + p + '/')
        
        self.tab2_detectionOutputPaths.sort(reverse=True)

        # return 1 if there isn't any detection record
        if len(self.tab2_detectionOutputPaths) == 0:
            return 1
        
        # return 0 if there is at least one detection record
        return 0

        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load('zh-tw_for_DetectionDemo')
    app.installTranslator(translator)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
