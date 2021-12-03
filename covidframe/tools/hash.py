import cv2
from wand.image import Image


# Based on
# https://www.pyimagesearch.com/2020/04/20/detect-and-remove-duplicate-images-from-a-dataset-for-deep-learning/
def dhash(image, hashSize=8):
    # convert the image to grayscale and resize the grayscale image,
    # adding a single column (width) so we can compute the horizontal
    # gradient
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))

    # compute the (relative) horizontal gradient between adjacent
    # column pixels
    diff = resized[:, 1:] > resized[:, :-1]

    # convert the difference image to a hash and return it
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


# Based on
# https://stackoverflow.com/a/3384123/5107192
def imhash(image):
    with Image(filename=image) as i:
        return i.signature


if __name__ == "__main__":

    PATH_IMAGE = "/mnt/Archivos/dataset-xray/Covid19-dataset/train/Covid/04.png"
    print(dhash(PATH_IMAGE))
    print(imhash(PATH_IMAGE))
