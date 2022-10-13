# Lab 7

This is a Python script I made using a plugin called NumPy, Which provides a large library of mathematical functions for array operations and supports various higher-order operations.

First start the virtual environment.

```Powershell
pip install virtualenv
virtualenv ~/venv/webscraping
~/venv/webscraping/Scripts/activate.ps1
pip install numpy
```

Example 1
Enter the following code in python

```Python
import numpy as np
the_array = np.array([51,1,5,90,3,6,39,99])
```

The purpose is to set some arrays

```Python
array1 = np.where(the_array > 50, 0, the_array)
print(array1)
```
Then find numbers greater than 50 in these arrays and convert to 0.

Example 2
Enter the following code in python

```Python
import numpy as np
array1 = np.array([0,2,4,6,7,8,9,20])
```

The same is done to set some arrays

```Python
filter_array2 = np.logical_or(array1 < 7, array1 == 20)
print(array1[filter_array2])
```

Then pick the numbers less tahn 7 and the specified number and output them.

Example 3
Enter the following code in python

```Python
import numpy as np
array1 = np.arange(200).reshape((20,10))
```

The purpose here is to split 1-200 into 20 rows and 10 columns

```Python
np.random.shuffle(array1)
rows = array1[:5,:]
columns = array1[:,:3]
print(rows)
print(columns)
```

Then randomly pick 5 rows of numbers and 3 columns of numbers and output them.

Don't forget to deactivate virtualenv when done.

```Powershell
deactivate
```
