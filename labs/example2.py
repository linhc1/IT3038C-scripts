import numpy as np

array1 = np.array([0,2,4,6,7,8,9,20])

filter_array2 = np.logical_or(array1 < 7, array1 == 20)
print(array1[filter_array2])
