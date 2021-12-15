import matplotlib.pyplot as plt


def show_results_from_history(log):
    val_loss = log.history['val_loss']
    val_acc = log.history['val_accuracy']

    fig, axes = plt.subplots(1, 2, figsize=(14, 4))
    ax1, ax2 = axes
    ax1.plot(log.history['loss'], label='train')
    ax1.plot(val_loss, label='test')
    ax1.set_xlabel('epoch')
    ax1.set_ylabel('loss')
    ax2.plot(log.history['accuracy'], label='train')
    ax2.plot(val_acc, label='test')
    ax2.set_xlabel('epoch')
    ax2.set_ylabel('accuracy')
    for ax in axes:
        ax.legend()

    return axes, fig
