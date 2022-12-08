import math

#This program uses the logistic equation and calculates the growth of a
#bacteria colony after 24 hours
t_0=0.0 #inital time
t_1=24.0 #time
inital_pop = 5000 #population at t_0
B = 50000 #maximum carrying capacity
k=0.2 #growth rate
C = (B/inital_pop)-1 #Calculating C as a function of inital_pop and B


N = B/(1+C*math.exp(-k*t_1)) #population growth after 24 hours
print("The population of the bacteria colony after 24 hours is %8.3f"%N)
#output: The population of the bacteria colony after 24 hours is 46551.999
