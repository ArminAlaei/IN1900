import math

#This program calculates the two roots of the following quadratic equation:
# 6x^2 -5x+1 = 0

a = 6.0
b = -5.0
c = 1.0

x_1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating root 1
x_2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a) #Calculating root 2

print("Root 1 is %5.2f and root 2 is %5.2f "%(x_1,x_2))
#output: Root 1 is  0.50 and root 2 is  0.33
