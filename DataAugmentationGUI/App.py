import os
import sys
import xml.etree.ElementTree as ET
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile, Qt
from DataAugmentationGUI import Ui_MainWindow
# from DataAugmentation_2005_GUI import doAugmentation
import imageio
import imgaug as ia
import matplotlib.pyplot as plt
import math
from imgaug import augmenters as iaa


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.runButton.clicked.connect(self.runButtonClick)

        self.ui.imageSourceBrowseButton.clicked.connect(self.imageSourceBrowseButtonClick)

        self.ui.xmlSourceBrowseButton.clicked.connect(self.xmlSourceBrowseButtonClick)

        self.ui.destinationBrowseButton.clicked.connect(self.destinationBrowseButtonClick)

    def findAugmenterIndex(self, augmenterList, target, augmenterHistory):
        for i in range(len(augmenterList)):
            if augmenterList[i][0].text == target and augmenterHistory[i] == 0:
                return i
        return - 1  # normally, it won't be executed

    # generate the augmenters according to the discription in configuration file
    def generateAugmenter(self, augmenters, target, augmenterHistory):
        if target == 'Add':
            augmenter = iaa.Add(int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'AdditiveGaussianNoise':
            augmenter = iaa.AdditiveGaussianNoise(scale=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text) * 255)
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'AveragePooling':
            augmenter = iaa.AveragePooling(kernel_size=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'CoarseDropout':
            augmenter = iaa.CoarseDropout(size_percent=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Crop':
            augmenter = iaa.Crop(percent=(float(
                augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text),
                float(
                augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][1].text),
                float(
                augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][2].text),
                float(
                augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][3].text)),
                keep_size=False)
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Dropout':
            augmenter = iaa.Dropout(p=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'ElasticTransformation':
            augmenter = iaa.ElasticTransformation(alpha=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text),
                                                  sigma=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][1].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Emboss':
            augmenter = iaa.Emboss(alpha=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text),
                                   strength=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][1].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Flipud':
            augmenter = iaa.Flipud(p=1)
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Fliplr':
            augmenter = iaa.Fliplr(p=1)
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'GammaContrast':
            augmenter = iaa.GammaContrast(gamma=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'GaussianBlur':
            augmenter = iaa.GaussianBlur(sigma=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'HistogramEqualization':
            augmenter = iaa.HistogramEqualization(to_colorspace=augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text)
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'JpegCompression':
            augmenter = iaa.JpegCompression(compression=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'LinearContrast':
            augmenter = iaa.LinearContrast(alpha=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'LogContrast':
            augmenter = iaa.LogContrast(gain=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex( augmenters, target, augmenterHistory)] = 1
        elif target == 'MotionBlur':
            augmenter = iaa.MotionBlur(k=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text),
                                       angle=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][1].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Pad':
            augmenter = iaa.Pad(percent=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Rot':
            augmenter = iaa.Rot90(k=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text), keep_size=False)
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        elif target == 'Sharpen':
            augmenter = iaa.Sharpen(alpha=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text),
                                    lightness=int(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][1].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        else:
            augmenter = iaa.SigmoidContrast(cutoff=float(augmenters[self.findAugmenterIndex(augmenters, target, augmenterHistory)][2][0].text))
            augmenterHistory[self.findAugmenterIndex(augmenters, target, augmenterHistory)] = 1
        return augmenter

    def doAugmentation(self):
        # argparse
        # parser = ArgumentParser()
        # parser.add_argument("conf", help="the path of augmenter configurations")
        # arguments = parser.parse_args()
        # configurationFile = os.path.abspath('.') + '/' + arguments.conf
        # for debugging
        configurationFile = os.path.abspath('.') + '\\AugmenterConfigurations.xml'

        # parsing configuration file
        configurationTree = ET.parse(configurationFile)
        configurationRoot = configurationTree.getroot()

        # the directory of images to augment
        imageSourceDirectory = configurationRoot.findall('imageSourceDirectory')[0].text
        # the directory of original xml
        xmlSourceDirectory = configurationRoot.findall('xmlSourceDirectory')[0].text
        # the directory to save augmented images
        imageDestinationDirectory = configurationRoot.findall('imageDestinationDirectory')[0].text
        # mkdir if destination directory doesn't exist
        if os.path.isdir(imageDestinationDirectory) is False:
            os.mkdir(imageDestinationDirectory)

        # deprecated deprecated
        # xmlDestinationDirectory = configurationRoot.findall('xmlDestinationDirectory')[0].text

        # augmenters. Visit https://github.com/aleju/imgaug to find more augmenters.
        # sequential augmentation. Applies all the augmenters(sequentially) to an image, generates an image that contains all the augmenters.
        # seq = iaa.Sequential([
        #     iaa.SigmoidContrast(cutoff=0.6, gain=7)])  # modify "iaa.Add(-45), iaa.Crop(precent=0.2), iaa.GaussianBlur(2)" to get the augmentation type you want
        # seperate augmentation. Applies one augmenter to an image and generated augmented image.
        # deprecated deprecated

        # load all of the augmenters in configuration file
        augmenters = configurationRoot.findall('augmenter')

        # file type
        # be aware of the file type, ex: jpg v.s. JPG and jpg v.s. jpeg, they are different!
        fileType = '.jpg'

        # getting addresses of images to augment
        imageAddresses = []
        totalImageCount = 0
        finishPartCount = 0
        for f in os.listdir(imageSourceDirectory):
            if (f.__contains__(fileType)):
                imageAddresses.append(imageSourceDirectory + '/' + f)
                totalImageCount += 1

        # counting the number of augmenters actually using
        augmenterCount = 0
        for a in augmenters:
            if a[1].text == 'Yes':
                augmenterCount += 1

        # data for showing augmented samples
        originalImageToShow = None
        imagesToShow = []
        titlesToShow = []

        # augmentation
        augmenterHistory = [0]*len(augmenters)
        # print('starting augmentation')
        self.ui.stateTextEdit.append('Starting augmentation...')
        for a in augmenters:
            if a[1].text == 'Yes':  # checking whether the user want to use this augmenter
                # print('part: ' + str(finishPartCount + 1) + '/' + str(augmenterCount))
                self.ui.stateTextEdit.append('part: ' + str(finishPartCount + 1) + '/' + str(augmenterCount))

                # generate imgaug augmenter
                seq = self.generateAugmenter(augmenters, a[0].text, augmenterHistory)

                finishImageCount = 0
                for address in imageAddresses:
                    boundingBoxes = []

                    # getting target image and xml file
                    image = imageio.imread(address)
                    augmentedTree = ET.parse(address.replace(imageSourceDirectory, xmlSourceDirectory).replace(fileType, '.xml'))
                    augmentedRoot = augmentedTree.getroot()

                    # getting bounding boxes
                    for obj in augmentedRoot.iter('object'):
                        boundingBoxes.append(ia.BoundingBox(x1=int(obj[4][0].text),
                                                            y1=int(obj[4][1].text),
                                                            x2=int(obj[4][2].text),
                                                            y2=int(obj[4][3].text),
                                                            label=obj[0].text))
                    BBS = ia.BoundingBoxesOnImage(boundingBoxes, shape=image.shape)

                    # augmentation
                    augmentedImage, augmentedBBS = seq(image=image, bounding_boxes=BBS)

                    # xml handling
                    for fileName in augmentedRoot.iter('filename'):
                        newNameAttributes = '_'
                        if a[0].text == 'Crop':
                            newNameAttributes = newNameAttributes + a[0].text
                            if a[2][0].text == '0' and a[2][3].text == '0':
                                newNameAttributes = newNameAttributes + '=' + 'topLeft'
                            elif a[2][0].text == '0' and a[2][1].text == '0':
                                newNameAttributes = newNameAttributes + '=' + 'topRight'
                            elif a[2][2].text == '0' and a[2][1].text == '0':
                                newNameAttributes = newNameAttributes + '=' + 'bottomRight'
                            elif a[2][2].text == '0' and a[2][3].text == '0':
                                newNameAttributes = newNameAttributes + '=' + 'bottomLeft'
                        elif a[0].text == 'Flipud' or a[0].text == 'Fliplr':
                            newNameAttributes = newNameAttributes + a[0].text
                        elif a[0].text == 'Rot':
                            newNameAttributes = newNameAttributes + a[0].text + '=' + a[2][0].text
                        elif a[0].text == 'Add':
                            newNameAttributes = newNameAttributes + a[0].text + '=' + a[2][0].text
                        else:
                            newNameAttributes = newNameAttributes + a[0].text
                            for args in a[2]:
                                newNameAttributes = newNameAttributes + '_' + args.tag + '=' + args.text.replace('.', 'p')
                        newName = str(fileName.text.replace(fileType, newNameAttributes)) + fileType
                        fileName.text = newName
                    for folder in augmentedRoot.iter('folder'):
                        newFolder = str(a[0].text)
                        folder.text = newFolder
                    for path in augmentedRoot.iter('path'):
                        newPath = str(imageDestinationDirectory) + '/' + a[0].text + '/' + newName
                        path.text = newPath
                    for size in augmentedRoot.iter('size'):
                        size[0].text = str(augmentedImage.shape[1])
                        size[1].text = str(augmentedImage.shape[0])
                        size[2].text = str(augmentedImage.shape[2])
                    i = 0
                    for obj in augmentedRoot.findall('object'):
                        if augmentedBBS.bounding_boxes[i].is_fully_within_image(augmentedImage.shape):
                            obj[4][0].text = str(augmentedBBS.bounding_boxes[i].x1)
                            obj[4][1].text = str(augmentedBBS.bounding_boxes[i].y1)
                            obj[4][2].text = str(augmentedBBS.bounding_boxes[i].x2)
                            obj[4][3].text = str(augmentedBBS.bounding_boxes[i].y2)
                        elif augmentedBBS.bounding_boxes[i].is_partly_within_image(augmentedImage.shape):
                            augmentedBBS.bounding_boxes[i].clip_out_of_image(augmentedImage.shape)
                            obj[4][0].text = str(augmentedBBS.bounding_boxes[i].x1)
                            obj[4][1].text = str(augmentedBBS.bounding_boxes[i].y1)
                            obj[4][2].text = str(augmentedBBS.bounding_boxes[i].x2)
                            obj[4][3].text = str(augmentedBBS.bounding_boxes[i].y2)
                        else:
                            augmentedRoot.remove(obj)
                        i += 1

                    # draw bounding boxes on image (uncomment to enable)
                    # augmentedImage = augmentedBBS.draw_on_image(
                    #     augmentedImage, size=5, color=[0, 0, 255])

                    # saving new xml file
                    # mkdir if destination directory doesn't exist
                    if os.path.isdir(newPath.replace(newName, '')) is False:
                        os.mkdir(newPath.replace(newName, ''))
                        os.mkdir(newPath.replace(newName, '/xmlFile'))
                    augmentedTree.write(newPath.replace(newName, '/xmlFile/' + newName).replace(fileType, '.xml'))  # for saving jpg and xml into seperate directories

                    # saving new image
                    imageio.imsave(newPath, augmentedImage)

                    # collecting samples to show
                    if finishPartCount is 0 and finishImageCount is 0:
                        originalImageToShow = image
                    if finishImageCount is 0:  # sample images to show later
                        imagesToShow.append(augmentedImage)
                        titlesToShow.append(a[0].text)

                    finishImageCount += 1
                    # print(str(finishImageCount) + '/' + str(totalImageCount) + ', saved to: ' + newPath)
                    self.ui.stateTextEdit.append(str(finishImageCount) + '/' + str(totalImageCount) + ', saved to: ' + newPath)
                finishPartCount += 1
                # print('')
                self.ui.stateTextEdit.append('')

        # showing augmented samples
        # checking whether the user want to show augmented samples
        if configurationRoot.findall('showAugmentedSamples')[0].text == 'Yes':
            totalSampleCount = math.ceil(augmenterCount/3)
            for i in range(0, augmenterCount, 3):
                # print('showing sample: ' + str(int((i / 3) + 1)) + '/' + str(totalSampleCount))
                self.ui.stateTextEdit.append('showing sample: ' + str(int((i / 3) + 1)) + '/' + str(totalSampleCount))
                plt.figure(figsize=(12.8, 7.2))
                plt.axis('off')
                if augmenterCount - i is 1:
                    plt.subplot(1, 2, 1)
                elif augmenterCount - i is 2:
                    plt.subplot(1, 3, 1)
                else:
                    plt.subplot(2, 2, 1)
                plt.imshow(originalImageToShow)
                plt.title('Original')
                j = 0
                while j < 3 and i + j < len(imagesToShow):
                    if augmenterCount - i is 1:
                        plt.subplot(1, 2, j+2)
                    elif augmenterCount - i is 2:
                        plt.subplot(1, 3, j+2)
                    else:
                        plt.subplot(2, 2, j+2)
                    plt.imshow(imagesToShow[i+j])
                    plt.title(titlesToShow[i+j])
                    plt.axis('off')
                    j += 1
                plt.show()

        # print('Augmentation finished.')
        self.ui.stateTextEdit.append('Augmentation finished.')

    def runButtonClick(self):
        configTree = ET.parse(os.path.abspath('.') + '/AugmenterConfigurations.xml')
        configRoot = configTree.getroot()
        for i in configRoot.iter('imageSourceDirectory'):
            i.text = str(self.ui.imageSourceLineEdit.text())
        for i in configRoot.iter('xmlSourceDirectory'):
            i.text = str(self.ui.xmlSourceLineEdit.text())
        for i in configRoot.iter('imageDestinationDirectory'):
            i.text = str(self.ui.destinationLineEdit.text())
        for i in configRoot.iter('showAugmentedSamples'):
            if self.ui.showCheckBox.isChecked():
                i.text = 'Yes'
            else:
                i.text = 'No'
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
        self.doAugmentation()

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