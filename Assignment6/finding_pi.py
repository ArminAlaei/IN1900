import numpy as np

#defining initial guess
x_0 = 3.14
print(f"x_0 = {x_0}")
for i in range(1,3): #iterate for x_1 and x_2
    x_1 = x_0 - (np.sin(x_0)/np.cos(x_0)) #function to approximate
    print(f"x_{i} = {x_1:.13f}")
    x_0 = x_1
print(f"numpy value of pi = {np.pi:.13f}")

"""
Run example:
user$ python3 finding_pi.py

output:

x_0 = 3.14
x_1 = 3.1415926549364
x_2 = 3.1415926535898
numpy value of pi = 3.1415926535898

"""
