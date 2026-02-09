# file name analysis.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")
t = data["t"]
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

plt.plot(t, x)
plt.title("x vs t")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.grid()
plt.show()

plt.plot(t, v)
plt.title("v vs t")
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
plt.grid()
plt.show()

plt.plot(t, E)
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
