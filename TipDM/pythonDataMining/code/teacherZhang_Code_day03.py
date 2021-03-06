# -*- coding: utf-8 -*-
# @Time    : 2017-10-18 21:40
# @Author  : Storm
# @File    : teacherZhang_Code.py

import numpy as np

a = np.array([1, 2, 3])
print(a)

a = np.array([[1, 2, 3], [3, 6, 1]])
d = ((1, 2, 3), (2, 4, 1))
np.array(d)
print(a)
print(np.zeros([3, 4]))
print(np.ones([2, 3]))
print(np.identity(5))

res = np.arange(1, 10, 2)
res = np.linspace(1, 10, 10)
print(np.reshape(res, [5, 2]))

# 访问数组：索引与切片
a = np.array([2, 6, 10, 2, 1.5])
print(a[1:5])
a = np.array([[1, 10, 2], [11, 0, 3], [1, 0.5, 30]])
print(a)
print(a[1, 2])
a[1, 2] = 1  # 修改

# 科学运算
a = np.array([[1, 10, 2], [11, 0, 3], [1, 0.5, 30]])
print(a)
print(a[a < 10])
print(a ** 2)
print(sum(a))
print(a.sum())

# ======pandas包======
import pandas as pd

da = pd.read_table('/Users/zhangmin/Desktop/西安理工大学/day04/4-1data.txt', sep=',')
import numpy as np
from pandas import DataFrame, Series

ser = Series([1, 2, 'a'], index=['a', 'b', 'c'])
ser = Series({'a': [1, 2, 3], 'b': ['1', '2', '3']})

# 数据框的构造：
d = [[2, 3, 2, 4], [3, 5, 2, 7], [8, 4, 5, 1], [6, 4, 62, 1], [5, 8, 9, 4], [0, 1, 7, 3]]
df = DataFrame(d, index=['a', 'b', 'c', 'd', 'e', 'f'], columns=list('ABCD'))
DataFrame(index=['1', '2'], columns=['b', 'c'])  # 生成缺失值矩阵
DataFrame(0, index=['1', '2'], columns=['b', 'c'])  # 生成全零矩阵
d = {'color': ['blue', 'green', 'yellow', 'red', 'white'],
     'object': ['ball', 'pen', 'pencil', 'paper', 'mug'],
     'price': [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = DataFrame(d, index=['a', 'b', 'c', 'd', 'e'])
print(frame.index)
print(frame.columns)

# 索引
df[:2]
df[:'c']  # 行
df['A']  # 列
df[['A', 'C']]

# loc只能通过行列名称索引
df.loc[:, ['A', 'B']]
df.loc['a':'c', ['A', 'B']]
df.loc['a', ['A', 'b']]
df.loc[[True, True, False, False, False], ['A', 'B']]  # loc也能通过逻辑值索引

# iloc只能通过位置索引
df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[3, 2]
df.iloc[[1, 2], :]

# ix既能通过行列名称也能通过位置索引
df.ix[:, ['A', 'B']]
df.ix[3:5, 0:2]
df.ix[3, 2]
df.ix[[0, 2], 1] = 1
df = DataFrame(index=['0', '1', '2', '3'], columns=['b', 'c'])  # 生成缺失值矩阵
df.ix[[True, False, True, True], 1] = 1  # 逻辑索引

# 练习3
x = range(1, 101)
y = range(101, 201)
dis = np.zeros([100, 100])
for i in range(0, 100):
    for j in range(0, 100):
        dis[i, j] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5

# 练习4：数据索引
from pandas import DataFrame, Series
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data
y = iris.target
da = DataFrame(x, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
da.ix[:, 'Species'] = y
da.ix[0:50, 'Species'] = 'setosa'
da.ix[50:100, 'Species'] = 'versicolor'
da.ix[100:150, 'Species'] = 'virginica'

# 练习5:K-means算法实现=========
from pandas import DataFrame, Series  # 导入所需要的两个函数

n = 50  # 待聚类样本个数
x = Series(range(1, n + 1))  # 样本的x坐标值
y = Series(range(n, n + n))  # 样本的y坐标值
center0 = Series([x[0], y[0]])  # 初始第一个类中心
center1 = Series([x[1], y[1]])  # 初始第二个类中心
dis = DataFrame(index=range(0, n), columns=['dis_cen0', 'dis_cen1', 'class'])  # 初始数据框


# =====自定义求最小值位置的函数=====
def which_min(x):
    if x[0] <= x[1]:
        z = 0
    else:
        z = 1
    return z


# =====主循环开始=====
while True:
    for i in range(0, n):  # 求各样本至各类中心的距离
        dis.ix[i, 0] = ((x[i] - center0[0]) ** 2 + (y[i] - center0[1]) ** 2) ** 0.5
        dis.ix[i, 1] = ((x[i] - center1[0]) ** 2 + (y[i] - center1[1]) ** 2) ** 0.5
        dis.ix[i, 2] = which_min(dis.ix[i, 0:2])  # 样本归类
    index0 = dis.ix[:, 2] == 0  # 第一类样本序号
    index1 = dis.ix[:, 2] == 1  # 第二类样本序号
    # ====求新类中心===
    center0_new = Series([x[index0].mean(), y[index0].mean()])
    center1_new = Series([x[index1].mean(), y[index1].mean()])
    # ====判定类中心是否发生变化,若否则中止while循环====
    if sum(center0 == center0_new) + sum(center1 == center1_new) == 4:
        break
    # ====更新类中心
    center0 = center0_new
    center1 = center1_new
print(dis)  # 输出结果

# =======决策树======
import os
import pandas as pd
from random import sample
from sklearn.tree import DecisionTreeClassifier

os.chdir('/Users/zhangmin/Desktop/贵阳/张敏课件/1.2')
data = pd.read_table('1.2-1data.txt', sep=',', encoding='utf-8', header=0)
data = data.ix[:, [0, 1, 2, 3, 4, 5, 7]]
tr_index = sample(range(0, 930), int(930 * 0.8))
te_index = [i for i in range(0, 930) if i not in tr_index]
tr_data = data.ix[tr_index, :]
te_data = data.ix[te_index, :]
# 决策树
modle = DecisionTreeClassifier(criterion='gini').fit(tr_data.ix[:, 0:6], tr_data.ix[:, 6])  # 模型训练
res = modle.predict(te_data.ix[:, 0:6])
print(sum(res == te_data.ix[:, 6]) / len(res))  # 准确率

# =======神经网络======
from random import sample  # 导入抽样函数
from sklearn.datasets import load_iris  # 导入鸢尾花数据集
from sklearn.neural_network import MLPClassifier  # 导入神经网络包

iris = load_iris()  # 读取数据
tr_index = sample(range(0, 50), 40)
tr_index.extend(sample(range(50, 100), 40))
tr_index.extend(sample(range(100, 150), 40))  # 训练集样本序号
td_index = [i for i in range(0, 150) if i not in tr_index]  # 测试集样本序号
tr_in = iris.data[tr_index, :]  # 训练集输入
tr_out = iris.target[tr_index]  # 训练集目标输出
te_in = iris.data[te_index, :]  # 测试集输入
net = MLPClassifier(hidden_layer_sizes=10, max_iter=1000).fit(tr_in, tr_out)  # 神经网络模型
res_net = net.predict(te_in)
print(res_net)  # 模型输出
print(iris.target[te_index])  # 实际值
print(sum(res_net == iris.target[te_index]) / len(res_net))  # 准确率
