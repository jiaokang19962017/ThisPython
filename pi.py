# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:09:24 2016

@author: Administrator
"""
import random as rd
import math

sample_count = 100000000  # 采样次数
inner = 0  # 落在圆内的点
i = 0  # while 计数器
while i < sample_count:
    x_i = rd.uniform(-1, 1)
    y_i = rd.uniform(-1, 1)
    if (math.pow(x_i, 2) + math.pow(y_i, 2)) < 1:
        inner = inner + 1

    i = i + 1

pi = 4 * (inner * 1.0) / (sample_count)
print(pi)