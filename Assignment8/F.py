# 8.3. Make a function class
import numpy as np
import matplotlib.pyplot as plt

class F:
    def __init__(self,n,m):

        self.n = n
        self.m = m

    def __call__(self, x):
        return (np.sin(self.n*x)*np.cos(self.m*x))

u = F(n = 2, m = 3)
v = F(n = 1, m = 4)

#defining x values from 0 to 2pi and smooth curve
x = np.linspace(0,2*np.pi,151)

plt.plot(x,u(x), label = "U(x)")
plt.plot(x,v(x), label = "V(x)")
plt.legend()
plt.show()

"""
Run example:

user$ python3 atm_moon.py

output:
(plot attached)

"""
