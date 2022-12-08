import math

#3.8

#This code segment is from population_table.py and
#computes the two lists t,N that we need in task 3.8
inital_pop = 5000 #population at t_0
B = 50000 #maximum carrying capacity
k=0.2 #growth rate
C = (B/inital_pop)-1 #Calculating C as a function of inital_pop and B

t = []
N=[]
for i in range(0,49,4):
    formula = B/(1+C*math.exp(-k*i))
    t.append(i)
    N.append(formula)

#3.8 a)
print()
print("Task 3.8 a)")
print()
tN1 = [t,N] #Creating the list tN1 with the two lists t and N simply by putting brackets around.

for x,y in zip(tN1[0],tN1[1]): #Here we iterate over the lists in the tN1 list using the zip function and print the values
    print(f"{x} , {y}")

print()
print("Task 3.8 b)")
print()
#3.8 b)
#Here we create a nested list from t and N and we use list comprehension to iterate over the lists.
tN2 = [list(l) for l in zip(t, N)]
#Looping over the tN2 list with two variables and printing them, also formatting the
#population to be integer and not float as described in the task.
for v,b in tN2:
    b = int(b)
    print(f"{v} , {b}")
#    print(f"{v},{b:.0f}") #We can print the value formatted as a float with 0 decimals also,
#    please uncomment if you wish to do so, also
#    please note that this does NOT actually convert float to int.


"""
Run code:
Go to terminal and use cd in the commandline to navigate to the folder where this file
is located and type (if you have python3 or type python otherwise):

usr$ python3 population_table2.py

The output in the terminal will be:

output:

Task 3.8 a)

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

Task 3.8 b)

0 , 5000
4 , 9912
8 , 17748
12 , 27526
16 , 36580
20 , 42924
24 , 46551
28 , 48389
32 , 49263
36 , 49666
40 , 49849
44 , 49932
48 , 49969


"""
