import numpy as np
the_array = np.array([51,1,5,90,3,6,39,99])

array1 = np.where(the_array > 50, 0, the_array)
print(array1)
