import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=10)

# edgecolors数据点轮廓
# plt.scatter(x_values, y_values, edgecolors='none', s=10)

# c数据点颜色，可以使用RGB类型，取值为0~1
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=10)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=10)

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=10)

plt.axis([0, 1100, 0, 1100000])

plt.show()

# 将图片保存到指定目录中
# plt.savefig('squares_plot.png')
