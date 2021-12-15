import cv2
from covidframe.tools.image import load_image

# Based on
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html


def apply_equalization_to_file(filename):
    x = load_image(filename)

    return apply_equalization(x)


def apply_equalization_to_array(img_array, type_equalization=None,
                                clip_limit=0.2, tile_size=8):

    return [apply_equalization(img, type_equalization, clip_limit, tile_size)
            for img in img_array]


def apply_equalization(x, type_equalization=None,
                       clip_limit=0.2, tile_size=8):

    if type_equalization == "simple":
        return simple_equalization(x)

    return clahe_equalization(x, clip_limit, tile_size)


def simple_equalization(x):
    return cv2.equalizeHist(x)


def clahe_equalization(x, clip_limit=0.2, tile_size=8):
    clahe = cv2.createCLAHE(clipLimit=clip_limit,
                            tileGridSize=(tile_size, tile_size))
    return clahe.apply(x)
