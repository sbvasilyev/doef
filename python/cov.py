# Задача 1

from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

num_of_fractions = 51
t = np.linspace(0, 2, num_of_fractions)
dt = t[1] - t[0]

print(f"t:      [{t[0]}, {t[1]}, {t[2]}, ..., {t[-1]}]")
print(f"dt:     {dt}")

def f(y):
    return np.sum(y[1:] ** 2 + ((y[1:] - y[:-1]) / dt) ** 2)

y0 = [0.2 for _ in t]
print(f"y0:     [{y0[0]}, ..., {y0[-1]}]")

EPS = 10e-6
bounds = [(None, None) for _ in t]
bounds[0]  = (0.0 - EPS, 0.0 + EPS)
bounds[-1] = (1.0 - EPS, 1.0 + EPS)
print(f"bounds: [{bounds[0]}, {bounds[1]}, ..., {bounds[-2]}, {bounds[-1]}]")

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)

def f_analytical(t):
  return (np.exp(t) - np.exp(-t)) / (np.exp(2) - np.exp(-2))

plt.plot(t, res.x, 'r', t, f_analytical(t), '--b')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(('y численный', 'y аналитический'))
plt.savefig("./img/cov-1.png")
plt.clf()

# Задача 2
num_of_fractions = 41
t = np.linspace(0, 1, num_of_fractions)
dt = t[1] - t[0]

def f(y):
  return np.sum(y[1:] ** 2 + (t[1:] ** 2) * (((y[1:] - y[:-1]) / dt) ** 2))

y0 = [1.5 for _ in t]
bounds = [(None, None) for _ in t]
bounds[0]  = (1.0 - EPS, 1.0 + EPS)
bounds[-1] = (2.0 - EPS, 2.0 + EPS)

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)

plt.plot(t, res.x)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig("./img/cov-2.png")
plt.clf()

# Задача 3
num_of_fractions = 41
t = np.linspace(0, 1, num_of_fractions)
dt = t[1] - t[0]

def f(y):
  return np.sum(y[1:] ** 2 + (t[1:] ** 2) * (((y[1:] - y[:-1]) / dt) ** 2))

y0 = [1.5 for _ in t]
bounds = [(None, None) for _ in t]
bounds[0]  = (1.0 - EPS, 1.0 + EPS)

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)

plt.plot(t, res.x)
plt.xlabel('t')
plt.ylabel('y')
plt.savefig("./img/cov-3.png")
plt.clf()

num_of_fractions = 41
t = np.linspace(0, 1, num_of_fractions)
dt = t[1] - t[0]


def f(y):
    return np.sum(y[1:] * (((y[1:] - y[:-1]) / dt) ** 2), axis=0)

y0 = [0.5 for _ in t]
bounds = [(None, None) for _ in t]
bounds[0], bounds[-1] = (1.0 - EPS, 1.0 + EPS), (4.0 - EPS, 4.0 + EPS)

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)

def f_analytical(t):
    return (7 * t + 1) ** (2 / 3) 

plt.plot(t, res.x, 'r', t, f_analytical(t), '--b')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(("y численный", "y аналитический"))
plt.savefig("./img/cov-4.png")
plt.clf()

num_of_fractions = 41
t = np.linspace(0, 1, num_of_fractions)
dt = t[1] - t[0]

def f(y):
    dy = (y[1:] - y[:-1]) / dt
    d2y = (dy[1:] - dy[:-1]) / dt
    return np.sum(y[2:] + d2y**2)

y0 = [0.5 for _ in t]
bounds = [(None, None) for _ in t]
bounds[0], bounds[-1] = (1.0 - EPS, 1.0 + EPS), (4.0 - EPS, 4.0 + EPS)

res = minimize(f, y0, method='l-bfgs-b', bounds=bounds)

plt.plot(t, res.x, 'r')
plt.xlabel('t')
plt.ylabel('y')
plt.savefig("./img/cov-5.png")
plt.clf()
