import math

#This program calculates the growth of a bankdeposit

P = 1000 #inital ammount
n = 3 #number of years deposited
r = 5 #interest rate in percent

A = P*(1+r/100)**n

print("1000 euros have grown to %7.3f euros after 5 years with an interest rate of 5 percent"%A)
#output: 1000 euros have grown to 1157.625 euros after 5 years with an interest rate of 5 percent
