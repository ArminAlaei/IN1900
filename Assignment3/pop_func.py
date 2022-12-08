import math

#4.1 Implement a function for population growth

def population(t,k,B,C):
    #defining empty lists
    tid = []
    pop=[]
    #creating a for loop to compute the
    #population over n + 1 uniformly spaced t values throughout the interval [0, 48], where n = 12.
    for i in range(0,t+1,4):
        formula = B/(1+C*math.exp(-k*i))
        tid.append(i)
        pop.append(formula) #appending the computed values to the empty lists outside the loop

    #Here we use the zip function and iterate through the two lists and print out the values
    #from both lists.
    for time,value in zip(tid,pop):
        print(f"{time} , {value}")

population(48,0.2,50000,9)



"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 pop_func.py

The output in the terminal will be:

output:

0 , 5000.0
4 , 9912.8449251102
8 , 17748.946156447553
12 , 27526.04324880943
16 , 36580.19548913157
20 , 42924.32248791071
24 , 46551.99938399246
28 , 48389.558080265095
32 , 49263.31561672727
36 , 49666.27875017217
40 , 49849.49621300692
44 , 49932.262009407634
48 , 49969.54063534766



"""
