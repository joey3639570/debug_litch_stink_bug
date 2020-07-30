import os
import sys
import xml.etree.ElementTree as ET
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile, Qt
from DataAugmentationGUI import Ui_MainWindow
from DataAugmentation_2005_GUI import doAugmentation

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.runButton.clicked.connect(self.runButtonClick)

        self.ui.imageSourceBrowseButton.clicked.connect(self.imageSourceBrowseButtonClick)

        self.ui.xmlSourceBrowseButton.clicked.connect(self.xmlSourceBrowseButtonClick)

        self.ui.destinationBrowseButton.clicked.connect(self.destinationBrowseButtonClick)

    
    def runButtonClick(self):
        configTree = ET.parse(os.path.abspath('.') + '/AugmenterConfigurations.xml')
        configRoot = configTree.getroot()
        for i in configRoot.iter('imageSourceDirectory'):
            i.text=str(self.ui.imageSourceLineEdit.text())
        for i in configRoot.iter('xmlSourceDirectory'):
            i.text=str(self.ui.xmlSourceLineEdit.text())
        for i in configRoot.iter('imageDestinationDirectory'):
            i.text=str(self.ui.destinationLineEdit.text())
        for i in configRoot.iter('showAugmentedSamples'):
            if self.ui.showCheckBox.isChecked():
                i.text='Yes'
            else:
                i.text='No'
        checkedAugmenter = []
        for i in range(self.ui.augmenterListWidget.count()):
            if self.ui.augmenterListWidget.item(i).checkState() == Qt.Checked:
                checkedAugmenter.append('Yes')
            else:
                checkedAugmenter.append('No')
        count = 0
        for i in configRoot.iter('augmenter'):
            if checkedAugmenter[count] == 'Yes':
                i[1].text = str('Yes')
            else:
                i[1].text = str('No')
            count += 1
        configTree.write(os.path.abspath('.') + '/AugmenterConfigurations.xml')
        doAugmentation()

    def imageSourceBrowseButtonClick(self):
        source = QFileDialog.getExistingDirectory(self)
        self.ui.imageSourceLineEdit.setText(source)

    def xmlSourceBrowseButtonClick(self):
        source = QFileDialog.getExistingDirectory(self)
        self.ui.xmlSourceLineEdit.setText(source)

    def destinationBrowseButtonClick(self):
        source = QFileDialog.getExistingDirectory(self)
        self.ui.destinationLineEdit.setText(source)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())