import numpy as np
import matplotlib.pyplot as plt

def abs_approx(x,N):
    for n in range(1,N+1):
        f = (((np.pi/2)-(np.pi/4) * (np.cos(2*n*x-x))/((2*n-1)**2))) #appriximation function
        #plotting x and the function for each iteration and labeling the curves
        plt.plot(x,f, label=str(n))

    presis = np.abs(x)  #numpy function for absolute value
    plt.plot(x,presis, label = "numpy abs function")
    plt.legend()    #plotting legend
    plt.show()
    return f

x = np.linspace(-np.pi,np.pi)  #defining x to go from -pi to pi
#calling the function with x and N=4
print(abs_approx(x,4))

"""
Run example:
user$ python3 approx_abs.py

output:

[1.58682486 1.58078995 1.56722964 1.55635512 1.55635512 1.56722964
 1.58078995 1.58682486 1.58078995 1.56722964 1.55635512 1.55635512
 1.56722964 1.58078995 1.58682486 1.58078995 1.56722964 1.55635512
 1.55635512 1.56722964 1.58078995 1.58682486 1.58078995 1.56722964
 1.55635512 1.55635512 1.56722964 1.58078995 1.58682486 1.58078995
 1.56722964 1.55635512 1.55635512 1.56722964 1.58078995 1.58682486
 1.58078995 1.56722964 1.55635512 1.55635512 1.56722964 1.58078995
 1.58682486 1.58078995 1.56722964 1.55635512 1.55635512 1.56722964
 1.58078995 1.58682486]
"""
