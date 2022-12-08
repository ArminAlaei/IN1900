from math import *

#4.5. Half-wave rectifier


def f(x):
    if sin(x)>0:
        return sin(x)
    else:
        return 0

#Test function for the f(x) function to check if computed is equal to expected
def test_f():
    x_val = [-1.0,pi/2]
    exp_val = [0.0,1.0]
    tol = 1e-14
    for x,exp in zip(x_val,exp_val):
        assert abs(f(x)-exp) < tol, \
            f"Failed for x = {x}, expected {exp}, but got {f(x)}"
test_f()
svar = f(pi/2)
print(svar)



"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 half_wave.py

The output in the terminal will be:

output:

1.0


"""
