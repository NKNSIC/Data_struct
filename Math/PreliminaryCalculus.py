#算符包
import sympy
from sympy import *

#极限
x = Symbol('x')
f = sin(x) / x

result = limit(f, x, 0)
print('x-->0,limf =',result)

result = limit(f, x, oo)
print('x-->OO,limf =',result)

#导数
f = exp(2*x)*sin(x)

print(f.diff())
print(f.diff().evalf(subs = {x:1}))

#隐函数
x, y = symbols('x y')
F = log(sqrt(x*x + y*y)) - atan(y/x)
dydx = idiff(F, y, x)
print(dydx)

#级数
n = Symbol('n', intger = True)
expr = 1/(n**2)
S = Sum(expr, (n, 1, oo))
print(S.doit())

#泰勒级数
x = Symbol('x')
f = (1 + x)**(1/5)
print(series(f, x, 1, 4))

#偏导数
u, v = symbols('u v')
x, y, z = symbols('x y z')
u = x * y
v = x + y
z = E**u*sin(v)
print(z.diff(x))
print(z.diff(y))

#不定积分
x = symbols('x')
fx = 1 / sin(x)
Fx = integrate(fx, x)
Fx = simplify(Fx)
print(Fx)

#定积分
x = symbols('x')
fx = E**x*cos(x)
Fx = integrate(fx, (x, 1, 2))
#精确解
print(Fx)
#数值解
print(N(Fx))

x = symbols('x')
fx = sin(x) / x
Fx = integrate(fx, (x, 0, oo))
#精确解
print(Fx)
#数值解
print(N(Fx))