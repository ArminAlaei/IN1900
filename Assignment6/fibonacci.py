import numpy as np
from numpy import zeros
x = zeros(16) #numpy array with zeroes
x[0] = 1 #filling in the numpy array with x_0 and x_1
x[1] = 1
for i in range(1,16):
    x[i] = x[i-1] + x[i-2] #calculating the equation
    print(f"i = {i}  x[i] = {x[i]}")


"""
Run example:
user$ python3 fibonacci.py

output:

i = 1  x[i] = 1.0
i = 2  x[i] = 2.0
i = 3  x[i] = 3.0
i = 4  x[i] = 5.0
i = 5  x[i] = 8.0
i = 6  x[i] = 13.0
i = 7  x[i] = 21.0
i = 8  x[i] = 34.0
i = 9  x[i] = 55.0
i = 10  x[i] = 89.0
i = 11  x[i] = 144.0
i = 12  x[i] = 233.0
i = 13  x[i] = 377.0
i = 14  x[i] = 610.0
i = 15  x[i] = 987.0

"""
