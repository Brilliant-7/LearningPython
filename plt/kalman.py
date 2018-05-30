# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

points = 200

# 状态变量 xkk = fk * xk + w
fk = 0.5
w = np.random.randn(points)
xk = np.zeros(points)

for k in range(1, points):
    xk[k] = fk * xk[k - 1] + w[k]

# 观测变量
h = 2
v = np.random.randn(points)
zk = np.zeros(points)

for k in range(1, points):
    zk[k] = h * xk[k - 1] + v[k]

# 卡尔曼滤波
q = np.var(w)
r = np.var(v)

print(q)
print(r)

yk = np.zeros(points)
yk[0] = zk[0]
xupdate = zk[0]
pkk = 0

for k in range(1, points):
    xpredict = fk * xupdate
    pk = fk * pkk * fk + q
    kk = pk * h * (1 / (h * pk * h + r))
    xupdate = xpredict + kk * (zk[k] - h * xpredict)
    pkk = (1 - kk * h) * pk

    yk[k] = xupdate

tx = range(points)

plt.figure('kalman')
plt.plot(tx, xk, tx, zk, tx, yk)
plt.title(u'卡尔曼滤波仿真')
plt.legend([u'状态变量', u'观测变量', u'预测更新'])

plt.show()
