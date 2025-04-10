import numpy as np

a = []
b = []

while(1):
    k = eval(input("输入"))
    if(k == 0):
        break
    else:
        a.append(k)

while(1):
    l = eval(input("输入"))
    if(l == 0):
        break
    else:
        b.append(l)

vector_N = np.array(a)
vector_Y = np.array(b)




#向量去均值化

vector_N_average = np.mean(vector_N)
vector_Y_average = np.mean(vector_Y)

vector_N_do_mean = vector_N - vector_N_average
vector_Y_do_mean = vector_Y - vector_Y_average

#模型准确度标准差程度计算区

vector_N_std = np.std(vector_N_do_mean)
vector_Y_std = np.std(vector_Y_do_mean)

#程度与准确度调和均值

H_old = 2 / ( 1/vector_N_std + 1/vector_N_average )
H_new = 2 / ( 1/vector_Y_std + 1/vector_Y_average )


print("未使用正则化处理标准差：{0}".format(vector_N_std))
print("使用正则化处理标准差：{0}".format(vector_Y_std))
print('-'*27)
print("未使用正则化处理调和均值：{0}".format(H_old))
print("使用正则化处理调和均值：{0}".format(H_new))