import numpy as np
array1 = np.arange(200).reshape((20,10))
np.random.shuffle(array1)
rows = array1[:5,:]
columns = array1[:,:3]
print(rows)
print(columns)
