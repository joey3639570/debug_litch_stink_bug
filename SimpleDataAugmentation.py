import imageio
import imgaug as ia
import os
from imgaug import augmenters as iaa
 
# please modify the variables below to the directory you store the photos
imageSourceDirectory = 'C:\\Users\\user\\Pictures\\test'
imageDestinationDirectory = 'C:\\Users\\user\\Desktop\\SimpleDataAugmentation'
 
# please refer to https://github.com/aleju/imgaug
seq = iaa.Sequential([iaa.Sharpen(alpha=0.8, lightness=1)])
fileExtension = '.jpg'
 
imageAddresses = []
totalImageCount = 0
finishCount = 0
for f in os.listdir(imageSourceDirectory):
    if (f.__contains__(fileExtension)):
        imageAddresses.append(imageSourceDirectory + '/' + f)
        totalImageCount += 1

os.mkdir(imageDestinationDirectory)

print('start augmentation.')
for address in imageAddresses:
    image = imageio.imread(address)
    augmentedImage = seq(image=image)
    newPath = str(address.replace(imageSourceDirectory, imageDestinationDirectory))
    imageio.imsave(newPath ,augmentedImage)
    finishCount += 1
    print(str(finishCount) + '/' + str(totalImageCount) + ', saved to: ' + newPath)
print('Augmentation finished.')