import numpy as np
from covidframe.tools.image import prepare_image_to_fft, get_fourier

# Based on
# https://medium.com/@elvisdias/introduction-to-fourier-transform-with-opencv-922a79cddf36


def apply_homomorfic(x):

    return homomorphic(x, yh, yl, c, d0)


def homomorphic(x, yh, yl, c, d0):

    img, dft_M, dft_N = prepare_image_to_fft(x)

    img = np.log(img + 1)

    fft = get_fourier(img)

    du = np.zeros(fft.shape, dtype=np.float32)
    #H(u, v)
    for u in range(dft_M):
        for v in range(dft_N):
            du[u, v] = np.sqrt((u - dft_M / 2.0) * (u - dft_M / 2.0) +
                               (v - dft_N / 2.0) * (v - dft_N / 2.0))

    du2 = cv2.multiply(du, du) / (d0 * d0)
    re = np.exp(- c * du2)
    H = (yh - yl) * (1 - re) + yl
    # S(u, v)
    filtered = cv2.mulSpectrums(complex, H, 0)
    # inverse DFT (does the shift back first)
    filtered = np.fft.ifftshift(filtered)
    filtered = cv2.idft(filtered)
    # normalization to be representable
    filtered = cv2.magnitude(filtered[:, :, 0], filtered[:, :, 1])
    return x
