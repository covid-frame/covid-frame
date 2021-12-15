from matplotlib.pylab import plt
import numpy as np
from covidframe.tools.image import load_image_list


def plot_images_from_files(files, n_cols):

    im_array = load_image_list(files)

    return plot_images(im_array, n_cols)


def plot_images(img_array, n_cols, figsize=(16, 16)):
    num_imagenes = len(img_array)
    num_filas = int(np.ceil(num_imagenes / n_cols))
    fig = plt.figure(figsize=figsize)

    for i in range(num_imagenes):
        ax = fig.add_subplot(num_filas, n_cols, i + 1)
        ax.imshow(img_array[i], cmap='Greys_r')
        ax.axis('off')


def plot_image_and_histogram(img, figsize=(12, 4)):

    fig = plt.figure(figsize=figsize)
    axes = fig.subplots(1, 2)

    axes[0].imshow(img, cmap='Greys_r')
    axes[0].axis('off')
    plot_histogram(img, ax=axes[1])


def plot_histogram(img, ax=None, plot_cumsum=True):

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

    ax.hist(img.flatten(), 256, [0, 256])

    if plot_cumsum:
        hist, _ = np.histogram(img.flatten(), 256, [0, 256])

        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()
        ax.plot(cdf_normalized)
