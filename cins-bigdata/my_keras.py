# -*- coding: utf-8 -*-
# @Time    : 2017-11-03 13:36
# @Author  : Storm
# @File    : my_keras.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout

dataTrain = pd.read_csv('./data/train.csv', header=-1)  # 读取训练集
trainX = dataTrain.iloc[:, 0:8].as_matrix()
trainY = dataTrain.iloc[:, 8].as_matrix()

# trainX_denoising = dataTrain.iloc[:1999, 0:8].as_matrix()  #0.8053343
trainX_denoising = dataTrain.iloc[:1999, 4:7].as_matrix()  # 0.81998176
trainY_denoising = dataTrain.iloc[:1999, 8].as_matrix()

# 划分训练集一部分为测试集
trainX_split, testX_split, trainY_split, testY_split = \
    train_test_split(trainX_denoising, trainY_denoising, test_size=0.13, random_state=18)

kerasmodle = Sequential()
# 1.[0:8]
# kerasmodle.add(Dense(32, input_dim=8))
# kerasmodle.add(Activation('relu'))
# kerasmodle.add(Dropout(0.5))
# kerasmodle.add(Dense(64, input_dim=32))
# kerasmodle.add(Activation('tanh'))
# kerasmodle.add(Dropout(0.5))
# kerasmodle.add(Dense(1, input_dim=64))
# kerasmodle.add(Activation('linear'))

# 2.[4:7]
kerasmodle.add(Dense(16, input_dim=3))
kerasmodle.add(Activation('relu'))
kerasmodle.add(Dropout(0.5))
kerasmodle.add(Dense(1, input_dim=16))
kerasmodle.add(Activation('tanh'))

kerasmodle.compile(loss='mean_squared_error', optimizer='sgd')
kerasmodle.fit(trainX_split, trainY_split, epochs=20, batch_size=16)
res_keras = kerasmodle.predict(testX_split, batch_size=16)
# print('keras结果：', res_keras)

# print('划分测试集真实结果：', testY_split)
print('===================================================')
print('keras相关性：', np.corrcoef(np.reshape(res_keras, (1, len(testY_split))), testY_split))
