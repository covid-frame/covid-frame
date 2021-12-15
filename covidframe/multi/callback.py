import joblib.parallel
from collections import defaultdict

# patch joblib progress callback
# from https://stackoverflow.com/a/41815007/5107192


class BatchCompletionCallBack(object):
    completed = defaultdict(int)

    def __init__(self, time, index, parallel):
        self.index = index
        self.parallel = parallel

    def __call__(self, index):
        BatchCompletionCallBack.completed[self.parallel] += 1
        print("done with {}".format(
            BatchCompletionCallBack.completed[self.parallel]))
        if self.parallel._original_iterator is not None:
            self.parallel.dispatch_next()


joblib.parallel.BatchCompletionCallBack = BatchCompletionCallBack
