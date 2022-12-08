#Problem E.4. Decrease the length of the time steps

import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f, U0, T, n):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t


def f(u, t):
    return (np.cos(6*t))/(1+t+u)

n_vals = [20,30,35,40,50,100,1000,10000]
for ns in n_vals:
    u, t = ForwardEuler(f, U0=0,T=10, n=ns)
    plt.plot(t,u, label = "n = "+str(ns))
plt.grid()
plt.legend()
plt.show()



"""

Run example:

user$ python3 decrease_dt.py

plots are attached

"""
