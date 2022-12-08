import math

# 5.1. Quadratic with user input
#asking for user input as integer
a = int(input("Please enter a as integer: "))
b = int(input("Please enter b as integer: "))
c = int(input("Please enter c as integer: "))

x_1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating root 1
x_2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating root 2

print("Root 1 is %5.2f and root 2 is %5.2f "%(x_1,x_2))


"""
Run example:

user$ python3 quadratic_roots_input.py

output: Root 1 is  0.50 and root 2 is  0.33


"""
