# -*- coding: utf-8 -*-
# @Time    : 2017-10-24 16:55
# @Author  : Storm
# @File    : mytest.py
import random

import pandas as pd
from pandas import DataFrame
import numpy as np

n = 2000
data = DataFrame(np.random.random((n, 8)), columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
data.to_csv('./data/mytest.csv')
data = pd.read_csv('./data/mytest.csv')
a = np.random.random((n, 1))
# o=a+10*sin(f*f)+random()*(c+d)
for i in range(n):
    a[i] = data.loc[i, 'a'] + np.sin(data.loc[i, 'b'] + data.loc[i, 'f'] * data.loc[i, 'f']) * 10 + random.random() * (
        data.loc[i, 'c'] + data.loc[i, 'd'])
data['输出'] = a
data.to_csv('./data/mytest_train.csv')
