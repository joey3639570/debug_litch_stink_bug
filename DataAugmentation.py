import imageio
import imgaug as ia
import xml.etree.ElementTree as ET
import os
from imgaug import augmenters as iaa

# settings settings

# the directory of images to augment
imageSourceDirectory = 'C:\\Users\\path\\Pictures\\test'
# the directory of original xml
xmlSourceDirectory = 'C:\\Users\\path\\Pictures\\test\\xmlFile'
# the directory to save augmented images
imageDestinationDirectory = 'E:\\test'
xmlDestinationDirectory = 'E:\\test\\xmlFile'
# augmentat techniques. Visit https://github.com/aleju/imgaug to find more techniques.
seq = iaa.Sequential(
    [iaa.Rot90(k=1, keep_size=False)])  # modify "iaa.Add(-45), iaa.Crop(precent=0.2), iaa.GaussianBlur(2)" to get the augmentation type you want
# file names to augmented images
fileNameToAdd = '_Rotttt90'
# file type
# be aware of the file type, ex: jpg v.s. JPG and jpg v.s. jpeg, they are different!
fileType = '.jpg'

# settings settings

# getting fileNames of images to augment
imageAddresses = []
totalImageCount = 0
finishCount = 0
for f in os.listdir(imageSourceDirectory):
    if (f.__contains__(fileType)):
        imageAddresses.append(imageSourceDirectory + '\\' + f)
        totalImageCount += 1

# augmentation
print("start augmentation.")
for address in imageAddresses:
    boundingBoxes = []
    image = imageio.imread(address)
    # originalTree = ET.parse(address.replace(fileType, '.xml'))
    # originalRoot = originalTree.getroot()
    # augmentedTree = ET.parse(address.replace(fileType, '.xml')) # for jpg and xml are in the same directory
    augmentedTree = ET.parse(address.replace(
        imageSourceDirectory, xmlSourceDirectory).replace(fileType, '.xml'))  # for jpg and xml aren't in the same directory
    augmentedRoot = augmentedTree.getroot()

    # getting bounding boxes
    for obj in augmentedRoot.iter('object'):
        boundingBoxes.append(ia.BoundingBox(x1=int(obj[4][0].text), y1=int(
            obj[4][1].text), x2=int(obj[4][2].text), y2=int(obj[4][3].text), label=obj[0].text))
    BBS = ia.BoundingBoxesOnImage(boundingBoxes, shape=image.shape)

    # augmentation
    augmentedImage, augmentedBBS = seq(image=image, bounding_boxes=BBS)

    # xml handling
    for fileName in augmentedRoot.iter('filename'):
        newName = str(fileName.text.replace(
            fileType, fileNameToAdd)) + fileType
        fileName.text = str(newName)
    # for path in originalRoot.iter('path'):
        # path.text = str(address)  # modify the path in original xml
        # newPath = str(address.replace(sourceDirectory, destinationDirectory)) # save to another directory
        # path.text = newPath
    for path in augmentedRoot.iter('path'):
        # newPath = address.replace(fileType, fileNameToAdd) + fileType
        # path.text = str(newPath)
        newPath = str(imageDestinationDirectory) + '\\' + \
            newName  # save to another directory
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
            augmentedBBS.bounding_boxes[i].clip_out_of_image(
                augmentedImage.shape)
            obj[4][0].text = str(augmentedBBS.bounding_boxes[i].x1)
            obj[4][1].text = str(augmentedBBS.bounding_boxes[i].y1)
            obj[4][2].text = str(augmentedBBS.bounding_boxes[i].x2)
            obj[4][3].text = str(augmentedBBS.bounding_boxes[i].y2)
        else:
            augmentedRoot.remove(obj)
        i += 1

    # augmentedImage = augmentedBBS.draw_on_image(
    #     augmentedImage, size=5, color=[0, 0, 255])

    # saving new xml
    # originalTree.write(address.replace(fileType, '.xml'))
    augmentedTree.write(newPath.replace(imageDestinationDirectory, xmlDestinationDirectory).replace(
        fileType, '.xml'))  # for saving jpg and xml into seperate directories
    # saving new image
    imageio.imsave(newPath, augmentedImage)
    finishCount += 1
    print(str(finishCount) + "/" + str(totalImageCount) + ", saved to: " + newPath)

print("Augmentation finished.")
