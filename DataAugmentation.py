import imageio
import imgaug as ia
import xml.etree.ElementTree as ET
import os
from imgaug import augmenters as iaa

# settings
# directory of images to augment
dataDirectoryAddress = 'E:\\test'
# augmentat techniques. Visit https://github.com/aleju/imgaug to find more techniques.
seq = iaa.Sequential(
    [iaa.Noop()])  # modify "iaa.Add(-45), iaa.Crop(precent=0.2), iaa.GaussianBlur(2)" to get the augmentation type you want
#iaa.Add(-45), iaa.Crop(px=(30, 40, 30, 40), keep_size=False), iaa.GaussianBlur(2)
# file names to augmented images
fileNameToAdd = '_Noop'
# settings

# getting fileNames of images to augment
imageAddresses = []
for f in os.listdir(dataDirectoryAddress):
    if (f.__contains__('.jpg')):
        imageAddresses.append(dataDirectoryAddress + '\\' + f)

# augmentation
for address in imageAddresses:
    boundingBoxes = []
    image = imageio.imread(address)
    tree = ET.parse(address.replace('.jpg', '.xml'))
    root = tree.getroot()
    # getting bounding boxes
    for obj in root.iter('object'):
        boundingBoxes.append(ia.BoundingBox(x1=int(obj[4][0].text), y1=int(
            obj[4][1].text), x2=int(obj[4][2].text), y2=int(obj[4][3].text), label=obj[0].text))
    BBS = ia.BoundingBoxesOnImage(boundingBoxes, shape=image.shape)

    augmentedImage, augmentedBBS = seq(image=image, bounding_boxes=BBS)

    # dealing with bounding boxes that are out of the border of the image
    # augmentedBBS = augmentedBBS.remove_out_of_image()
    # augmentedBBS = augmentedBBS.clip_out_of_image()

    for fileName in root.iter('filename'):
        newName = str(fileName.text.replace('.jpg', fileNameToAdd)) + ".jpg"
        fileName.text = str(newName)
    for path in root.iter('path'):
        # newPath = str(path.text.replace('.jpg', fileNameToAdd)) + ".jpg"
        newPath = address.replace('.jpg', fileNameToAdd) + ".jpg"
        path.text = str(newPath)
    i = 0
    for obj in root.findall('object'):
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
            root.remove(obj)
        i += 1

    # augmentedImage = augmentedBBS.draw_on_image(
    #    augmentedImage, size=5, color=[0, 0, 255])

    # saving new xml
    tree.write(newPath.replace('.jpg', '.xml'))
    # saving new image
    imageio.imsave(newPath, augmentedImage)

print("Augmentation finished.")
