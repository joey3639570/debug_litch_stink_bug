# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataAugmentationGUI.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.runButton = QPushButton(self.centralwidget)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setGeometry(QRect(370, 470, 381, 31))
        self.imageSourceBrowseButton = QPushButton(self.centralwidget)
        self.imageSourceBrowseButton.setObjectName(u"imageSourceBrowseButton")
        self.imageSourceBrowseButton.setGeometry(QRect(40, 60, 93, 28))
        self.imageSourceLineEdit = QLineEdit(self.centralwidget)
        self.imageSourceLineEdit.setObjectName(u"imageSourceLineEdit")
        self.imageSourceLineEdit.setGeometry(QRect(140, 60, 611, 28))
        self.imageSourceLineEdit.setReadOnly(True)
        self.imageSourceLabel = QLabel(self.centralwidget)
        self.imageSourceLabel.setObjectName(u"imageSourceLabel")
        self.imageSourceLabel.setGeometry(QRect(20, 10, 171, 31))
        font = QFont()
        font.setPointSize(14)
        self.imageSourceLabel.setFont(font)
        self.imageSourceDescriptionLabel = QLabel(self.centralwidget)
        self.imageSourceDescriptionLabel.setObjectName(u"imageSourceDescriptionLabel")
        self.imageSourceDescriptionLabel.setGeometry(QRect(40, 40, 221, 16))
        self.destinationLabel = QLabel(self.centralwidget)
        self.destinationLabel.setObjectName(u"destinationLabel")
        self.destinationLabel.setGeometry(QRect(20, 190, 111, 31))
        self.destinationLabel.setFont(font)
        self.destinationLineEdit = QLineEdit(self.centralwidget)
        self.destinationLineEdit.setObjectName(u"destinationLineEdit")
        self.destinationLineEdit.setGeometry(QRect(140, 240, 611, 28))
        self.destinationLineEdit.setReadOnly(True)
        self.destinationDescriptionLabel = QLabel(self.centralwidget)
        self.destinationDescriptionLabel.setObjectName(u"destinationDescriptionLabel")
        self.destinationDescriptionLabel.setGeometry(QRect(40, 220, 251, 16))
        self.destinationBrowseButton = QPushButton(self.centralwidget)
        self.destinationBrowseButton.setObjectName(u"destinationBrowseButton")
        self.destinationBrowseButton.setGeometry(QRect(40, 240, 93, 28))
        self.xmlSourceLabel = QLabel(self.centralwidget)
        self.xmlSourceLabel.setObjectName(u"xmlSourceLabel")
        self.xmlSourceLabel.setGeometry(QRect(20, 100, 171, 31))
        self.xmlSourceLabel.setFont(font)
        self.xmlSourceLineEdit = QLineEdit(self.centralwidget)
        self.xmlSourceLineEdit.setObjectName(u"xmlSourceLineEdit")
        self.xmlSourceLineEdit.setGeometry(QRect(140, 150, 611, 28))
        self.xmlSourceLineEdit.setReadOnly(True)
        self.xmlSourceDescriptionLabel = QLabel(self.centralwidget)
        self.xmlSourceDescriptionLabel.setObjectName(u"xmlSourceDescriptionLabel")
        self.xmlSourceDescriptionLabel.setGeometry(QRect(40, 130, 221, 16))
        self.xmlSourceBrowseButton = QPushButton(self.centralwidget)
        self.xmlSourceBrowseButton.setObjectName(u"xmlSourceBrowseButton")
        self.xmlSourceBrowseButton.setGeometry(QRect(40, 150, 93, 28))
        self.augmentersLabel = QLabel(self.centralwidget)
        self.augmentersLabel.setObjectName(u"augmentersLabel")
        self.augmentersLabel.setGeometry(QRect(20, 280, 111, 31))
        self.augmentersLabel.setFont(font)
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
        self.augmenterListWidget.setObjectName(u"augmenterListWidget")
        self.augmenterListWidget.setGeometry(QRect(40, 310, 256, 151))
        self.showCheckBox = QCheckBox(self.centralwidget)
        self.showCheckBox.setObjectName(u"showCheckBox")
        self.showCheckBox.setGeometry(QRect(40, 470, 271, 16))
        font1 = QFont()
        font1.setPointSize(9)
        self.showCheckBox.setFont(font1)
        self.stateTextEdit = QTextEdit(self.centralwidget)
        self.stateTextEdit.setObjectName(u"stateTextEdit")
        self.stateTextEdit.setGeometry(QRect(370, 310, 381, 151))
        self.stateLabel = QLabel(self.centralwidget)
        self.stateLabel.setObjectName(u"stateLabel")
        self.stateLabel.setGeometry(QRect(350, 280, 111, 31))
        self.stateLabel.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuAugmentation = QMenu(self.menubar)
        self.menuAugmentation.setObjectName(u"menuAugmentation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAugmentation.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Add", None));
        ___qlistwidgetitem1 = self.augmenterListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"AdditiveGaussianNoise", None));
        ___qlistwidgetitem2 = self.augmenterListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"AveragePooling", None));
        ___qlistwidgetitem3 = self.augmenterListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CoarseDropout", None));
        ___qlistwidgetitem4 = self.augmenterListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Crop", None));
        ___qlistwidgetitem5 = self.augmenterListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Dropout", None));
        ___qlistwidgetitem6 = self.augmenterListWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ElasticTransformation", None));
        ___qlistwidgetitem7 = self.augmenterListWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Emboss", None));
        ___qlistwidgetitem8 = self.augmenterListWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Flipud", None));
        ___qlistwidgetitem9 = self.augmenterListWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fliplr", None));
        ___qlistwidgetitem10 = self.augmenterListWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"GammaContrast", None));
        ___qlistwidgetitem11 = self.augmenterListWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"GaussianBlur", None));
        ___qlistwidgetitem12 = self.augmenterListWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"HistogramEqualization", None));
        ___qlistwidgetitem13 = self.augmenterListWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"JpegCompression", None));
        ___qlistwidgetitem14 = self.augmenterListWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"LinearContrast", None));
        ___qlistwidgetitem15 = self.augmenterListWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"LogContrast", None));
        ___qlistwidgetitem16 = self.augmenterListWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"MotionBlur", None));
        ___qlistwidgetitem17 = self.augmenterListWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Pad", None));
        ___qlistwidgetitem18 = self.augmenterListWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Rot", None));
        ___qlistwidgetitem19 = self.augmenterListWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Sharpen", None));
        ___qlistwidgetitem20 = self.augmenterListWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"SigmoidContrast", None));
        self.augmenterListWidget.setSortingEnabled(__sortingEnabled)

        self.showCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show augmented samples?", None))
        self.stateLabel.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.menuAugmentation.setTitle(QCoreApplication.translate("MainWindow", u"Augmentation", None))
    # retranslateUi

