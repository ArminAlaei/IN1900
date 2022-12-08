import numpy as np
import matplotlib.pyplot as plt
import math

#a)
def plot_line(p1,p2):
    x_cor = [p1[0],p2[0]] #getting the coordinates in two lists
    y_cor = [p1[1],p2[1]]
    plt.plot(x_cor,y_cor) #plotting
    plt.show()
    return x_cor,y_cor
print("a)")
print(plot_line([0,0],[1,0])) #horizontal line
print(plot_line([0,0],[0,1])) #vertical line



#b)
def complete_graph(points):
    list_length = len(points)  # getting length of list of points
    #iterating from i to the length of the list -1
    for i in range(list_length-1):
        #new loop to go from i+1 to end of list and connect all the lines
        for x in range(i + 1, list_length):
            #defining the x and y coordinates using indexes
            x_c = [points[i][0], points[x][0]]
            y_c = [points[i][1], points[x][1]]
            plt.plot(x_c, y_c) #plotting each line using the x,y coordinates
    plt.show()
    return  points

a = np.sqrt(2)/2 #defining alpha
svar_1 = complete_graph([[0,0],[1,0],[0,1],[1,1]])
svar_2 = complete_graph([[1,0],[a,a],[0,1],[-a,a],[-1,0],[-a,-a],[0,-1],[a,-a]])

#running b) for both set of points given in the task
print("b)")
print(svar_1)
print(svar_2)

"""
Run example:

#The functions didnt have any returns so it automatically returned None but made
the plots. To "fix" this issue i return the x,y coordinates in a and in b) i return
the points that are used to make the plots. (nothing else was specified in the task
with regards to what the functions should return)
user$ python3 graph1.py

output:

a)
([0, 1], [0, 0])
([0, 0], [0, 1])
b)
[[0, 0], [1, 0], [0, 1], [1, 1]]
[[1, 0], [0.7071067811865476, 0.7071067811865476], [0, 1], [-0.7071067811865476, 0.7071067811865476], [-1, 0], [-0.7071067811865476, -0.7071067811865476], [0, -1], [0.7071067811865476, -0.7071067811865476]]


"""
