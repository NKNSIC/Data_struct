import sympy
from sympy import *
import math as m
import numpy as np
import matplotlib.pyplot as plt

#二重积分
#绘制区域
x, y = symbols('x y')
e1 = Eq(x + y, 2)
e2 = Eq(x**2, y)
sol = solve((e1, e2),(x, y))
print(sol)

x = np.linspace(-1, 2, 100)

y1 = 2 - x
y2 = x**2
y3 = 0*x + 2

#绘制
plt.plot(x, y1, c = 'g')
plt.plot(x, y2, c = 'r')
plt.plot(x, y3, c = 'b')

y = np.linspace(1, 2, 100)
x1 = 2 - y
x2 = np.sqrt(y)

plt.fill_betweenx(y, x1, x2, x1 <= x2, facecolor = 'lightgray')
plt.show()