#!/usr/bin/env python
# encoding: utf-8
'''
@Author  : pentiumCM
@Email   : 842679178@qq.com
@Software: PyCharm
@File    : __init__.py.py
@Time    : 2020/4/11 9:39
@desc	 : numpy计算矩阵的特征值，特征向量
'''

import numpy as np

mat = np.array([[-1, 3, -1, 1],
              [-3, 5, 1, -1],
              [10, -10, -10, 14],
              [4, -4, -4, 8]])

eigenvalue, featurevector = np.linalg.eig(mat)

print("特征值：", eigenvalue)
print("特征向量：", featurevector)

