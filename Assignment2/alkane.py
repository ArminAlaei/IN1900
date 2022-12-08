
#3.11

#In this task we compute and print the molar mass
#of the alkanes with two through nine Carbon atoms

#Given values in the task:
M_c = 12.011 #g/mol
M_h = 1.0079 #g/mol

for i in range(2,10): #Looping through n from 2 to 9 carbon atoms.
    m = 2*i+2 #calculating m
    mass = i*M_c+m*M_h #using m and computing the mass
    print(f"M(C{i}H{m}) = {mass:.3f} g/mol") #using f string to print the mass per iteration

"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 alkane.py

The output in the terminal will be:

output:
M(C2H6) = 30.069 g/mol
M(C3H8) = 44.096 g/mol
M(C4H10) = 58.123 g/mol
M(C5H12) = 72.150 g/mol
M(C6H14) = 86.177 g/mol
M(C7H16) = 100.203 g/mol
M(C8H18) = 114.230 g/mol
M(C9H20) = 128.257 g/mol


"""
