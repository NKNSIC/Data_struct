"""
本文件介绍了一般的矩阵乘法算法以及布尔矩阵乘法与离散数学的相适配性
0 1 1         1 1
1 0 0   0 1   0 1
0 1 0 x 1 0 = 1 0
1 0 1   1 1   1 1
"""
#一般的矩阵乘法算法
from numpy import dot
from numpy import array

a = [[1, 2], [3, 6]]
b = [[10, -4], [-5, 2]]

print(dot(a, b))         #答案正确

c = array([[0, 1, 1], [1, 0, 0], [0, 1, 0], [1, 0, 1]])
d = array([[0, 1], [1, 0], [1, 1]])

print(dot(c, d).astype(bool))   #可以计算值，但必须将结果值转换为bool值