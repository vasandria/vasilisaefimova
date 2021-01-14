from joblib import Parallel, delayed
import numpy as np
import time


def dotmartrix(A, B):
    return A.dot(B)


A1 = np.array([[3, 6, 7], [5, -3, 0]])
A2 = np.array([[1, 1], [2, 1], [3, -3]])

start = time.time()
test = Parallel(n_jobs=2)(delayed(dotmartrix)(A1, A2) for i in range(3))
stop = time.time()
print(test)
print('Время обработки: {:.2f} s'.format(stop - start))
