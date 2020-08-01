# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppMainWindowGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/Resources/WindowIcon.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setGeometry(QRect(370, 540, 381, 31))
        font = QFont()
        font.setFamily(u"Microsoft JhengHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.runButton.setFont(font)
        self.imageSourceBrowseButton = QPushButton(self.centralwidget)
        self.imageSourceBrowseButton.setObjectName(u"imageSourceBrowseButton")
        self.imageSourceBrowseButton.setGeometry(QRect(40, 70, 93, 28))
        font1 = QFont()
        font1.setFamily(u"Microsoft JhengHei UI")
        self.imageSourceBrowseButton.setFont(font1)
        self.imageSourceLineEdit = QLineEdit(self.centralwidget)
        self.imageSourceLineEdit.setObjectName(u"imageSourceLineEdit")
        self.imageSourceLineEdit.setGeometry(QRect(140, 70, 611, 28))
        self.imageSourceLineEdit.setReadOnly(True)
        self.imageSourceLabel = QLabel(self.centralwidget)
        self.imageSourceLabel.setObjectName(u"imageSourceLabel")
        self.imageSourceLabel.setGeometry(QRect(20, 10, 171, 31))
        font2 = QFont()
        font2.setFamily(u"Microsoft JhengHei UI")
        font2.setPointSize(14)
        self.imageSourceLabel.setFont(font2)
        self.imageSourceDescriptionLabel = QLabel(self.centralwidget)
        self.imageSourceDescriptionLabel.setObjectName(u"imageSourceDescriptionLabel")
        self.imageSourceDescriptionLabel.setGeometry(QRect(40, 40, 291, 21))
        self.imageSourceDescriptionLabel.setFont(font1)
        self.destinationLabel = QLabel(self.centralwidget)
        self.destinationLabel.setObjectName(u"destinationLabel")
        self.destinationLabel.setGeometry(QRect(20, 230, 141, 31))
        self.destinationLabel.setFont(font2)
        self.destinationLineEdit = QLineEdit(self.centralwidget)
        self.destinationLineEdit.setObjectName(u"destinationLineEdit")
        self.destinationLineEdit.setGeometry(QRect(140, 290, 611, 28))
        self.destinationLineEdit.setReadOnly(True)
        self.destinationDescriptionLabel = QLabel(self.centralwidget)
        self.destinationDescriptionLabel.setObjectName(u"destinationDescriptionLabel")
        self.destinationDescriptionLabel.setGeometry(QRect(40, 260, 311, 21))
        self.destinationDescriptionLabel.setFont(font1)
        self.destinationBrowseButton = QPushButton(self.centralwidget)
        self.destinationBrowseButton.setObjectName(u"destinationBrowseButton")
        self.destinationBrowseButton.setGeometry(QRect(40, 290, 93, 28))
        self.destinationBrowseButton.setFont(font1)
        self.xmlSourceLabel = QLabel(self.centralwidget)
        self.xmlSourceLabel.setObjectName(u"xmlSourceLabel")
        self.xmlSourceLabel.setGeometry(QRect(20, 120, 171, 31))
        self.xmlSourceLabel.setFont(font2)
        self.xmlSourceLineEdit = QLineEdit(self.centralwidget)
        self.xmlSourceLineEdit.setObjectName(u"xmlSourceLineEdit")
        self.xmlSourceLineEdit.setGeometry(QRect(140, 180, 611, 28))
        self.xmlSourceLineEdit.setReadOnly(True)
        self.xmlSourceDescriptionLabel = QLabel(self.centralwidget)
        self.xmlSourceDescriptionLabel.setObjectName(u"xmlSourceDescriptionLabel")
        self.xmlSourceDescriptionLabel.setGeometry(QRect(40, 150, 271, 21))
        self.xmlSourceDescriptionLabel.setFont(font1)
        self.xmlSourceBrowseButton = QPushButton(self.centralwidget)
        self.xmlSourceBrowseButton.setObjectName(u"xmlSourceBrowseButton")
        self.xmlSourceBrowseButton.setGeometry(QRect(40, 180, 93, 28))
        self.xmlSourceBrowseButton.setFont(font1)
        self.augmentersLabel = QLabel(self.centralwidget)
        self.augmentersLabel.setObjectName(u"augmentersLabel")
        self.augmentersLabel.setGeometry(QRect(20, 340, 141, 31))
        self.augmentersLabel.setFont(font2)
        self.augmenterListWidget = QListWidget(self.centralwidget)
        __qlistwidgetitem = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem.setCheckState(Qt.Unchecked);
        __qlistwidgetitem1 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        __qlistwidgetitem3 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem3.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem5 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem5.setCheckState(Qt.Unchecked);
        __qlistwidgetitem6 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem6.setCheckState(Qt.Unchecked);
        __qlistwidgetitem7 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem7.setCheckState(Qt.Unchecked);
        __qlistwidgetitem8 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem9.setCheckState(Qt.Unchecked);
        __qlistwidgetitem10 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem10.setCheckState(Qt.Unchecked);
        __qlistwidgetitem11 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem11.setCheckState(Qt.Unchecked);
        __qlistwidgetitem12 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem12.setCheckState(Qt.Unchecked);
        __qlistwidgetitem13 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem13.setCheckState(Qt.Unchecked);
        __qlistwidgetitem14 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem14.setCheckState(Qt.Unchecked);
        __qlistwidgetitem15 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem15.setCheckState(Qt.Unchecked);
        __qlistwidgetitem16 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem16.setCheckState(Qt.Unchecked);
        __qlistwidgetitem17 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem17.setCheckState(Qt.Unchecked);
        __qlistwidgetitem18 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem18.setCheckState(Qt.Unchecked);
        __qlistwidgetitem19 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem19.setCheckState(Qt.Unchecked);
        __qlistwidgetitem20 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem20.setCheckState(Qt.Unchecked);
        __qlistwidgetitem21 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem21.setCheckState(Qt.Unchecked);
        __qlistwidgetitem22 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem22.setCheckState(Qt.Unchecked);
        __qlistwidgetitem23 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem23.setCheckState(Qt.Unchecked);
        __qlistwidgetitem24 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem24.setCheckState(Qt.Unchecked);
        __qlistwidgetitem25 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem25.setCheckState(Qt.Unchecked);
        __qlistwidgetitem26 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem26.setCheckState(Qt.Unchecked);
        __qlistwidgetitem27 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem27.setCheckState(Qt.Unchecked);
        __qlistwidgetitem28 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem28.setCheckState(Qt.Unchecked);
        __qlistwidgetitem29 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem29.setCheckState(Qt.Unchecked);
        __qlistwidgetitem30 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem30.setCheckState(Qt.Unchecked);
        __qlistwidgetitem31 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem31.setCheckState(Qt.Unchecked);
        __qlistwidgetitem32 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem32.setCheckState(Qt.Unchecked);
        __qlistwidgetitem33 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem33.setCheckState(Qt.Unchecked);
        __qlistwidgetitem34 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem34.setCheckState(Qt.Unchecked);
        __qlistwidgetitem35 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem35.setCheckState(Qt.Unchecked);
        __qlistwidgetitem36 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem36.setCheckState(Qt.Unchecked);
        __qlistwidgetitem37 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem37.setCheckState(Qt.Unchecked);
        __qlistwidgetitem38 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem38.setCheckState(Qt.Unchecked);
        __qlistwidgetitem39 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem39.setCheckState(Qt.Unchecked);
        __qlistwidgetitem40 = QListWidgetItem(self.augmenterListWidget)
        __qlistwidgetitem40.setCheckState(Qt.Unchecked);
        self.augmenterListWidget.setObjectName(u"augmenterListWidget")
        self.augmenterListWidget.setGeometry(QRect(40, 400, 261, 131))
        self.showSampleCheckBox = QCheckBox(self.centralwidget)
        self.showSampleCheckBox.setObjectName(u"showSampleCheckBox")
        self.showSampleCheckBox.setGeometry(QRect(40, 540, 271, 21))
        self.showSampleCheckBox.setFont(font1)
        self.stateTextEdit = QTextEdit(self.centralwidget)
        self.stateTextEdit.setObjectName(u"stateTextEdit")
        self.stateTextEdit.setGeometry(QRect(370, 380, 381, 151))
        self.stateTextEdit.setFont(font)
        self.stateLabel = QLabel(self.centralwidget)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setGeometry(QRect(350, 340, 111, 31))
        self.stateLabel.setFont(font2)
        self.selectAllAugmentersCheckBox = QCheckBox(self.centralwidget)
        self.selectAllAugmentersCheckBox.setObjectName(u"selectAllAugmentersCheckBox")
        self.selectAllAugmentersCheckBox.setGeometry(QRect(40, 380, 261, 16))
        self.selectAllAugmentersCheckBox.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Do Data Augmentation", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.imageSourceBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.imageSourceLabel.setText(QCoreApplication.translate("MainWindow", u"Image source", None))
        self.imageSourceDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Click browse to specify image source", None))
        self.destinationLabel.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.destinationDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Click browse to specify image destination", None))
        self.destinationBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.xmlSourceLabel.setText(QCoreApplication.translate("MainWindow", u"XML source", None))
        self.xmlSourceDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Click browse to specify XML source", None))
        self.xmlSourceBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.augmentersLabel.setText(QCoreApplication.translate("MainWindow", u"Augmenters", None))

        __sortingEnabled = self.augmenterListWidget.isSortingEnabled()
        self.augmenterListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.augmenterListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Add_positive", None));
        ___qlistwidgetitem1 = self.augmenterListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Add_negative", None));
        ___qlistwidgetitem2 = self.augmenterListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"AdditiveGaussianNoise", None));
        ___qlistwidgetitem3 = self.augmenterListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"AveragePooling", None));
        ___qlistwidgetitem4 = self.augmenterListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CoarseDropout", None));
        ___qlistwidgetitem5 = self.augmenterListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Crop_topLeft", None));
        ___qlistwidgetitem6 = self.augmenterListWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Crop_topRight", None));
        ___qlistwidgetitem7 = self.augmenterListWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Crop_bottomRight", None));
        ___qlistwidgetitem8 = self.augmenterListWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Crop_bottomLeft", None));
        ___qlistwidgetitem9 = self.augmenterListWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Crop_center", None));
        ___qlistwidgetitem10 = self.augmenterListWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Dropout", None));
        ___qlistwidgetitem11 = self.augmenterListWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ElasticTransformation_strong", None));
        ___qlistwidgetitem12 = self.augmenterListWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ElasticTransformation_weak", None));
        ___qlistwidgetitem13 = self.augmenterListWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Emboss", None));
        ___qlistwidgetitem14 = self.augmenterListWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Flipud", None));
        ___qlistwidgetitem15 = self.augmenterListWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Fliplr", None));
        ___qlistwidgetitem16 = self.augmenterListWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"GammaContrast_low", None));
        ___qlistwidgetitem17 = self.augmenterListWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"GammaContrast_high", None));
        ___qlistwidgetitem18 = self.augmenterListWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"GaussianBlur", None));
        ___qlistwidgetitem19 = self.augmenterListWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"HistogramEqualization_Lab", None));
        ___qlistwidgetitem20 = self.augmenterListWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"HistogramEqualization_HLS", None));
        ___qlistwidgetitem21 = self.augmenterListWidget.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"HistogramEqualization_HSV", None));
        ___qlistwidgetitem22 = self.augmenterListWidget.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"JpegCompression", None));
        ___qlistwidgetitem23 = self.augmenterListWidget.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"LinearContrast_low", None));
        ___qlistwidgetitem24 = self.augmenterListWidget.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"LinearContrast_high", None));
        ___qlistwidgetitem25 = self.augmenterListWidget.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"LogContrast_low", None));
        ___qlistwidgetitem26 = self.augmenterListWidget.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"LinearContrast_high", None));
        ___qlistwidgetitem27 = self.augmenterListWidget.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"MotionBlur_degree_0", None));
        ___qlistwidgetitem28 = self.augmenterListWidget.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"MotionBlur_degree_72", None));
        ___qlistwidgetitem29 = self.augmenterListWidget.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"MotionBlur_degree_144", None));
        ___qlistwidgetitem30 = self.augmenterListWidget.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"MotionBlur_degree_216", None));
        ___qlistwidgetitem31 = self.augmenterListWidget.item(31)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"MotionBlur_degree_288", None));
        ___qlistwidgetitem32 = self.augmenterListWidget.item(32)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Pad_thin", None));
        ___qlistwidgetitem33 = self.augmenterListWidget.item(33)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Pad_thick", None));
        ___qlistwidgetitem34 = self.augmenterListWidget.item(34)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Rot_degree_90", None));
        ___qlistwidgetitem35 = self.augmenterListWidget.item(35)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Rot_degree_180", None));
        ___qlistwidgetitem36 = self.augmenterListWidget.item(36)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Rot_degree_270", None));
        ___qlistwidgetitem37 = self.augmenterListWidget.item(37)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Sharpen", None));
        ___qlistwidgetitem38 = self.augmenterListWidget.item(38)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"SigmoidContrast_low", None));
        ___qlistwidgetitem39 = self.augmenterListWidget.item(39)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"SigmoidContrast_medium", None));
        ___qlistwidgetitem40 = self.augmenterListWidget.item(40)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"SigmoidContrast_high", None));
        self.augmenterListWidget.setSortingEnabled(__sortingEnabled)

        self.showSampleCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show augmented samples", None))
        self.stateLabel.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.selectAllAugmentersCheckBox.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
    # retranslateUi

