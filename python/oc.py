from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt
import os

# Задача 1

# Инициализируем модель
m = GEKKO(remote=False)
nt = 101
m.time = np.linspace(0,2,nt)

# Задаём переменные
y = m.Var(value=1)
z = m.Var(value=5)
u = m.Var(value=0,lb=-1,ub=1)
t = m.Var(value=0)
# Отмечаем последнюю точку временной шкалы
p = np.zeros(nt)
p[-1] = 1.0
final = m.Param(value=p)


# Задаём уравнения
m.Equation(y.dt() == u)
m.Equation(t.dt() == 1)
m.Equation(z.dt() == 0.5 * y ** 2 + y**2 * t**2)

m.Obj(z * final)    # Целевая функция
m.options.IMODE = 6 # Задача оптимального управления/динамического программирования
m.solve()

plt.plot(m.time[1:], y.value[1:], 'k-', label=r'$y$')
plt.plot(m.time[1:],u.value[1:],'r--',label=r'$u$')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Value')
plt.savefig("./img/oc-1.png")
plt.clf()

# Задача 2

m = GEKKO(remote = False)
nt = 301
m.time = np.linspace(0,2,nt)

y = m.Var(value=2)
z = m.Var(value=0)
u = m.Var(value=0)
p = np.zeros(nt)
p[-1] = 1.0
final = m.Param(value=p)


m.Equation(y.dt()==y + u)
m.Equation(z.dt()==-y + (u ** 2) * 0.5 + u)
m.Obj(z*final)
m.options.IMODE = 6
m.solve(disp=False)

def u_a(t):
    return [np.exp(-elem + 2) - 2 for elem in t]

def y_a(t):
    return [2 + 0.5 * np.exp(2) * (np.exp(elem) - np.exp(-elem)) for elem in t]

plt.figure(figsize=(12, 10))
plt.subplot(2, 1, 1)
plt.plot(m.time, y.value, 'k-', label=r'$y$')
plt.plot(m.time, y_a(m.time), 'r--', label=r'$y^*$')
plt.legend(loc='best')
plt.ylabel('Value')
plt.subplot(2, 1, 2)
plt.plot(m.time[1:], u.value[1:], 'k-', label=r'$u$')
plt.plot(m.time[1:], u_a(m.time)[1:], 'r--', label=r'$u^*$')
plt.legend(loc='best')
plt.ylabel('Value')
plt.xlabel('Time')
plt.savefig("./img/oc-2.png")
plt.clf()

# Задача 3
m = GEKKO(remote = False)
nt = 301
m.time = np.linspace(0,2,nt)

y = m.Var(value=2)
z = m.Var(value=0)
u = m.Var(value=np.e-2, lb=np.e-2)
p = np.zeros(nt)
p[-1] = 1.0
final = m.Param(value=p)

m.Equation(y.dt()==y + u)
m.Equation(z.dt()==-y + (u ** 2) * 0.5 + u)
m.Obj(z*final)
m.options.IMODE = 6
m.solve(disp=False)

def u_a(t):
    return [np.exp(-elem + 2) - 2 if elem <= 1
            else np.e - 2
            for elem in t]

def y_a(t):
    return [2 + 0.5 * np.exp(2) * (np.exp(elem) - np.exp(-elem)) if elem <= 1
            else (1 + 0.5 * (np.e ** 2 - 1)) * np.exp(elem) - np.e + 2
            for elem in t]

plt.figure(figsize=(12, 10))
plt.subplot(2, 1, 1)
plt.plot(m.time, y.value, 'k-', label=r'$y$')
plt.plot(m.time, y_a(m.time), 'r--', label=r'$y^*$')
plt.legend(loc='best')
plt.ylabel('Value')
plt.subplot(2, 1, 2)
plt.plot(m.time[1:], u.value[1:], 'k-', label=r'$u$')
plt.plot(m.time[1:], u_a(m.time)[1:], 'r--', label=r'$u^*$')
plt.legend(loc='best')
plt.ylabel('Value')
plt.xlabel('Time')
plt.savefig("./img/oc-3.png")

# Задача 4

# необходимый оптимизатор IPOPT доступен только в gekko под Winsows
# для Linux/Max необходима опция remote=True
isLinux = os.name == 'posix'

m = GEKKO(remote=isLinux)
nt = 101
tm = np.linspace(0, 1, nt)
m.time = tm

y1 = m.Var(value=np.pi / 2.0)
y2 = m.Var(value=4.0)
y3 = m.Var(value=0.0)

p = np.zeros(nt)
p[-1] = 1.0
final = m.Param(value=p)

# FV = fixed value, то есть одинаковое для любого момента времени
T = m.FV(value=1.0, lb=0.1, ub=100.0)
# STATUS = 1 => участвует в оптимизации
T.STATUS = 1

# тоже самое, что u = m.Var(...)
u = m.MV(value=0, lb=-2, ub=2)
u.STATUS = 1

m.Equation(y1.dt() == u * T)
m.Equation(y2.dt() == m.cos(y1) * T)
m.Equation(y3.dt() == m.sin(y1) * T)

m.Equation(y2 * final <= 0)
m.Equation(y3 * final <= 0)

m.Obj(T)

m.options.IMODE = 6
m.solve(disp=False)

print('Найденное T: ' + str(T.value[0]))

# масштабируем исходную шкалу от 0 до 1
# можно брать любой элемент, они одинаковые
tm = tm * T.value[0]

plt.figure(1)
plt.plot(tm[1:], y1.value[1:], 'k-', linewidth=2, label=r'$y_1$')
plt.plot(tm[1:], y2.value[1:], 'b-', linewidth=2, label=r'$y_2$')
plt.plot(tm[1:], y3.value[1:], 'g--', linewidth=2, label=r'$y_3$')
plt.plot(tm[1:], u.value[1:], 'r--', linewidth=2, label=r'$u$')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Value')
plt.savefig("./img/oc-4.png")
plt.clf()
