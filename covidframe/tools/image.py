import cv2
import numpy as np

interpolation_mappings = {
    "linear": cv2.INTER_LINEAR,
    "area": cv2.INTER_AREA,
    "nearest": cv2.INTER_NEAREST,
    "cubic": cv2.INTER_CUBIC,
    "lanczo": cv2.INTER_LANCZOS4
}


def load_image_list(filename_path_list):

    return [load_image(filename_path)
            for filename_path in filename_path_list]


def load_image(filename_path):

    img = cv2.imread(filename_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray


def prepare_image_to_fft(image):

    height, width = image.shape
    dft_M = cv2.getOptimalDFTSize(height)
    dft_N = cv2.getOptimalDFTSize(width)

    padded = cv2.copyMakeBorder(
        image,
        0,
        dft_M - height,
        0,
        dft_N - width,
        cv2.BORDER_CONSTANT,
        0)

    return padded, dft_M, dft_N


def get_fourier(image):
    fft = cv2.dft(np.float32(image) / 255.0, flags=cv2.DFT_COMPLEX_OUTPUT)
    fft = np.fft.fftshift(fft)

    return fft


def resize_image(image, size, interpolation_type="linear"):

    if interpolation_type in interpolation_mappings.keys():
        interpolation = interpolation_type
    else:
        print("Warning: specified interpolation is not defined, fallback to "
              "linear interpolation")
        interpolation = "linear"

    return cv2.resize(image, size, interpolation_mappings[interpolation])


def to_equal_aspect_ratio(image, centered=True):

    original_size = image.shape
    selected_size = min(original_size)
    n_size = tuple([selected_size] * 2)

    return crop_image(image, n_size, centered=centered)


def crop_image(image, new_size, centered=True):

    original_size = image.shape
    new_height = min(new_size[0], original_size[0])
    new_width = min(new_size[1], original_size[1])
    n_size = (new_height, new_width)

    if centered:
        offset = np.divide(np.array(original_size) - np.array(n_size), 2)
        offset = offset.astype(int)

    else:
        offset = np.zeros(2)

    return image[offset[0]:offset[0] + n_size[0],
                 offset[1]:offset[1] + n_size[1]]
