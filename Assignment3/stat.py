import numpy as np
from math import *

#Task 4.8 Simple Statistical Functions

#List of numbers given in the task: [0.699, 0.703, 0.698, 0.688, 0.701]
######################################################################
# a) and b)
def mean(x_list):
    meen = sum(x_list)/len(x_list) #using the sum function and calculating the mean
    return meen



def test_mean():
    x = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(x)
    computed = mean(x)
    success = computed == expected
    msg = (f"computed {computed}, expected {expected}")
    assert success, msg


test_mean()
svar = mean([0.699, 0.703, 0.698, 0.688, 0.701])
print(f"The mean of the given list is {svar}")

######################################################################
# c) and d)

#using list comprehension and calculating sum(x_i-x(hat))and calculating the variance and standard deviation
def standard_deviation(x_list):
    m = mean(x_list)
    variance = sum([((i - m) ** 2) for i in x_list]) / len(x_list)                                                     #
    stddev = sqrt(variance)
    return  stddev

def test_standard_deviation():  #Using the test function to confirm that computed is equal to expected.
    x = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(x)
    computed = standard_deviation(x)
    success = computed == expected
    msg = (f"computed {computed}, expected {expected}")
    assert success, msg

test_standard_deviation()
s = standard_deviation([0.699, 0.703, 0.698, 0.688, 0.701])
print(f"The standard deviation of the given list is {s}")


"""
Run code:

***NOTE numpy must be installed in order for the instructions below to work***

Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):


usr$ python3 stat.py

The output in the terminal will be:

output:

The mean of the given list is 0.6977999999999999
The standard deviation of the given list is 0.005192301994298872


"""
