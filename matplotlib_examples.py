# encoding:utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(file, header=None)      # 读取预先生产的csv数据库

y = df.loc[0:100, 4].values  # 读取第四列的值
y = np.where(y == 'Iris-setosa',-1,1)  # 将数据库中为指定字符串的值用-1替代,否则用1替代

x = df.iloc[0:100, [0, 2]].values     # 抽取

plt.scatter(x[:50, 0], x[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('花瓣长度')
plt.ylabel('花茎长度')
plt.legend(loc='upper left')
plt.show()
