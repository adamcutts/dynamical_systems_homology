import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def double_gyre(X, t):
    # Set parameters
    A, epsilon, omega = 0.1, 0.1, np.pi / 5

    def a(t):
        return epsilon * np.sin(omega * t)

    def b(t):
        return 1 - 2 * epsilon * np.sin(omega * t)

    def f(x, t):
        return a(t) * x ** 2 + b(t) * x

    x, y = X
    vx = -np.pi*A*np.sin(np.pi*f(x,t))*np.cos(np.pi*y)
    vy = np.pi*A*np.cos(np.pi*f(x,t))*np.sin(np.pi*y)*(2*a(t)*x+b(t))
    return np.array([vx,vy])


def simulate_double_gyre(x0, y0, t_max, n):
    t = np.linspace(0, t_max, n)
    f = odeint(double_gyre, (x0, y0), t)
    x, y = f.T
    return x, y, t
