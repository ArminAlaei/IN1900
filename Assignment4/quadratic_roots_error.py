import math
import sys

# 5.3. Quadratic with exceptions
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    x_1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating root 1
    x_2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating root 2

    print("Root 1 is %5.2f and root 2 is %5.2f "%(x_1,x_2))

except IndexError:
    print("Please input numbers:")

    #Asking the user for input and calculating the roots
    A=int(input("Please enter A as integer: "))
    B=int(input("Please enter B as integer: "))
    C=int(input("Please enter C as integer: "))
    r_1 = (-B+math.sqrt((B**2)-(4*(A*C))))/(2*A) #Calculating roots
    r_2 = (-B-math.sqrt((B**2)-(4*(A*C))))/(2*A)

    print("Root 1 is %5.2f and root 2 is %5.2f "%(r_1,r_2))

"""
Run example #1 :

user$ python3 quadratic_roots_error.py 6 -5 1

output: Root 1 is  0.50 and root 2 is  0.33

Run example #2

user$ python3 quadratic_roots_error.py 

output: Please input numbers:
Please enter A as integer: 6
Please enter B as integer: -5
Please enter C as integer: 1
Root 1 is  0.50 and root 2 is  0.33


"""
