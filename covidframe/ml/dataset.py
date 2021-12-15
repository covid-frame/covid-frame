import tensorflow as tf


def get_dataset_from_slices(X, y, batch_size, prefetch_size=1,
                            parse_function=None,
                            parallel_calls=4):

    dataset = tf.data.Dataset.from_tensor_slices((X, y))
    dataset = dataset.shuffle(len(X))

    if parse_function is not None:
        dataset = dataset.map(
            parse_function,
            num_parallel_calls=parallel_calls)
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(prefetch_size)

    return dataset
