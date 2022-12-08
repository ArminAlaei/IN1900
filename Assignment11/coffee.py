from ODESolver import ForwardEuler
import matplotlib.pyplot as plt
import numpy as np
class Cooling:
    def __init__(self,h,T_s):
        self.h = h
        self.T = T_s

    def __call__(self, T, t):
        T =  -self.h*(T - T_s)
        return T


def estimate_h(t1,Ts,T0,T1):
    return (T1 - T0) / (t1*(T_s - T0))




def test_Cooling():
    ins = Cooling(h, 10)
    fe = ForwardEuler(ins)
    fe.set_initial_condition(U0=T0)
    timepoints = np.linspace(0, 10, 5)
    u, t = fe.solve(timepoints)
    expected = 5.434782608695652
    calculated = u[1]
    success = expected== calculated
    msg = "Failed"
    assert  msg

T0 = 95
T1 = 92
t0 = 0
t1 = 15

T_s = 20
h=estimate_h(t1=t1,Ts=T_s, T0=T0,T1=T1)


#c)
#defining the room temps
T_v = [20,25]

#Plotting for two different room temps
timepoints = np.linspace(0, 1500)
for tv in T_v:
    ins = Cooling(h, T_s=tv)
    fe = ForwardEuler(ins)
    fe.set_initial_condition(U0=T0)
    u,t = fe.solve(timepoints)
    plt.plot(t,u, label = "T_s = "+str(tv))
plt.xlabel("time (s)")
plt.ylabel("Temperature Celcius")
plt.grid()
plt.legend()
plt.show()


"""
I had issues understanding this problem, so the code is not correct, but
this is my attempt on this task.

Run example:

user$ python3 coffee.py

Plots attached

"""
