import sympy
from sympy import *

#函数是一个集合到另一个集合之间的关系
def f():
    X = set
    {'a', 'b', 'c'}
    Y = set
    {'A', 'B', 'C'}
    f = {('a','A'), ('b','B'), ('c','C')}
    return f

#复合函数
x = Symbol('x')
def a(x):
    return exp(x)
def b(x):
    return 2*x + 1
def h(x):
    return a(b(x))
print(h(x))

#数列
a_list = list[1, 2, 4, 7, 8]
#通项为2n的数列
def b(n):
    return 2*n
b_list = map(b,[1, 4, 5, 3, 2, 2])
print(list(b_list))