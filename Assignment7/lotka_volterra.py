
import numpy as np
import matplotlib.pyplot as plt

#Values given in the task
n = 500
a = 0.04
b = 0.1
c = 0.005
e = 0.2

#Initial conditions
rab = 100
fox = 20
r_pop = []
f_pop = []
for x in range(0,n+1):
    print(fox)
    rab = rab+(a*rab)-(c*rab*fox)
    fox = fox + (e*c*rab*fox) -(b*fox)
    r_pop.append(rab)
    f_pop.append(fox)

#convert the population lists to numpy arrays
r = np.array(r_pop)
f = np.array(f_pop)
tid = np.linspace(0,n,n+1)

plt.plot(tid,r, label = "Rabbit")
plt.plot(tid,f, label = "Fox")
plt.title("Lotka-Volterra two species model")
plt.legend()
plt.show()

"""
Run example:

user$ python3 lotka_volterra.py

output:

#Plot attached
"""
