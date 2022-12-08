import math
import sys

# 5.2. Quadratic with command line

#getting inputs from cmd line as floats
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])


x_1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating roots
x_2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a) 

print("Root 1 is %5.2f and root 2 is %5.2f "%(x_1,x_2))

"""
Run example:

user$ python3 quadratic_roots_cml.py 6 -5 1

output: Root 1 is  0.50 and root 2 is  0.33


"""
