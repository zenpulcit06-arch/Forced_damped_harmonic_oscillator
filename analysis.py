# file name analysis.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

data = pd.read_csv("data.csv")
time = data["t"]
x = data["x"]
v = data["v"]
a = data["a"]
E = data["E"]
const = pd.read_csv("const.csv")
b = const["b"].iloc[0]
k = const["k"].iloc[0]
m = const["m"].iloc[0]
F = const["F"].iloc[0]
omega = const["omega"].iloc[0]
phi = const["phi"].iloc[0]
dt = const["dt"].iloc[0]
T = const["T"].iloc[0]
Q = const["Q"].iloc[0]

def graphs():

    plt.plot(time, x)
    plt.title("x vs t")
    plt.xlabel("Time(s)")
    plt.ylabel("Position(m)")
    plt.grid()
    plt.show()

    plt.plot(time, v)
    plt.title("v vs t")
    plt.xlabel("Time(s)")
    plt.ylabel("Velocity(m/s)")
    plt.grid()
    plt.show()

    plt.plot(time, E)
    plt.title("E vs t")
    plt.xlabel("Time(s)")
    plt.ylabel("Energy(J)")
    plt.grid()
    plt.show()

    plt.plot(x, v)
    plt.title("Phase - Space analysis")
    plt.xlabel("Position(m)")
    plt.ylabel("Velocity(m/s)")
    plt.grid()
    plt.show()

def oscillator():
    def system(t,y):
        position , velocity = y
        dxdt = velocity
        dvdt = (1/m)*(-b*velocity - k*position + F*np.cos(omega*t + phi))
        return [dxdt,dvdt]
    
    y0 = [x.iloc[0],v.iloc[0]]
    t_span = (0,T)
    t_eval = np.linspace(0,T,len(time))

    sol = solve_ivp(system,t_span = t_span,y0 = y0,t_eval=t_eval)

    plt.plot(time,x,label = 'C verlet')
    plt.plot(sol.t,sol.y[0],label = 'scipy RK45')
    plt.xlabel("Time")
    plt.ylabel("Position (m)")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(time,v,label = 'C verlet')
    plt.plot(sol.t,sol.y[1],label = 'scipy RK45')
    plt.xlabel("Time")
    plt.ylabel("Velocity (m/s)")
    plt.legend()
    plt.grid()
    plt.show()
    
    



if __name__ == "__main__":
    graphs()
    oscillator()