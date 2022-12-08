
#3.4

#Here we found errors in the given script, fixed them and then we print the sum.
s=0
M = 3
k=1 #ERROR 1: k was not defined in the original code

for i in range(k,M+1): #ERROR 2: defining a start and and stop for the loop (M+1) since we include 3
    s+=1/(2*i)**2 #ERROR 3: parenthesis was not included in the original code
print(f"The sum is {s:.4f}")

"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 sum_for.py

The output in the terminal will be:

output: The sum is 0.3403

"""
