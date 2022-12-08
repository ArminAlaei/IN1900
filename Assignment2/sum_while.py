
#3.5

#Here we do the same as in 3.4 but we use a while loop to compute instead of a for loop.
s=0
M = 3
k=1

while k <M+1:
    s+=1/(2*k)**2
    k+=1 #k+1 so we increase each time we go through the loop and dont go forever on 1.
print(f"The sum is {s:.4f}")

"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 sum_while.py

The output in the terminal will be:

output: The sum is 0.3403

"""
