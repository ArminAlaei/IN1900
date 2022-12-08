import math
import sys

#5.4 Quadratic with raising Error
try:
    #Getting the inputs from cmd line as floats
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])


    x_1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating roots
    x_2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)

    print("Root 1 is %5.2f and root 2 is %5.2f "%(x_1,x_2))

except ValueError:
    raise ValueError("Please try another input, this set of numbers gives complex roots")



"""
Run example #1 with 1 1 1:

user$ python3 quadratic_roots_error2.py 1 1 1

output: Traceback (most recent call last):
  File "quadratic_roots_error2.py", line 18, in <module>
    raise ValueError("Please try another input, this set of numbers gives complex roots")
ValueError: Please try another input, this set of numbers gives complex roots


Run example #2 with 1 0 -1:

user$ python3 quadratic_roots_error2.py 1 0 -1

output: Root 1 is  1.00 and root 2 is -1.00

"""
