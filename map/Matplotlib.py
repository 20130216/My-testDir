# 导入模块
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('QT5Agg')

# 设置风格
plt.style.use('seaborn-v0_8-white')

# 中文显示问题，如果没有这段代码，图表不显示中文汉字
plt.rcParams['font.sans-serif'] = ['SimHei']

# 构建一个DataFrame

df = pd.DataFrame({'X': [1, 3, 5, 7]})
df['Y'] = df['X']**3
df


# 设置图像的大小
plt.figure(facecolor='white', figsize=(9, 6), dpi=100)
plt.plot(df['X'], df['Y'])
print("图像大小")
plt.show()

# 设置图像的标题
plt.title('zhexian map', fontsize=15, color='b')
print("图像标题")
plt.show()

# 设置图像的X、Y轴标题大小，颜色，与坐标轴的距离
plt.xlabel('X轴', fontsize=10, color='r', labelpad=15)
plt.ylabel('Y轴', fontsize=10, color='g', rotation=0, labelpad=15)
print("juli")
plt.show()

# 设置起始坐标点
plt.xlim([1, 8])
plt.ylim([1, 350])
print("坐标点")
plt.show()
# plt.xticks([1,2,3,4])只显示1,2,3,4
# plt.yticks([50,150,250,300])只显示50,150,250,300

# 图像的网格线进行设置
plt.grid(color='r', linestyle='-.')
print("网格线")
plt.show()

# 多个图的绘图方法

x = np.array([1, 3, 5])
y1 = x
y2 = x * 10
y3 = x * 20
y4 = x * 30

plt.figure(facecolor='white')
plt.plot(x, y1, label='A')
plt.plot(x, y2, label='B')
plt.plot(x, y3, label='C')
plt.plot(x, y4, label='D')

plt.legend()  # 显示图例

plt.show()

# 多表绘图

# 使用plt.subplots命令也可以作出同样的图。
# 使用面向对象绘图
fig, ax = plt.subplots(facecolor='white')
plt.plot(x, y1, label='A')
plt.plot(x, y2, label='B')
plt.plot(x, y3, label='C')
plt.plot(x, y4, label='D')

plt.legend()  # 显示图例
plt.show()


plt.figure(facecolor='white', figsize=(9, 6))

plt.subplot(221)
plt.plot(x, y1, label='A', color='r')
plt.xticks(fontsize=15)
plt.legend()  # 显示图例

plt.subplot(222)
plt.plot(x, y2, label='B', color='y')
plt.xticks(fontsize=15)
plt.legend()  # 显示图例

plt.subplot(223)
plt.plot(x, y3, label='C', color='b')
plt.xticks(fontsize=15)
plt.legend()  # 显示图例

plt.subplot(224)
plt.plot(x, y4, label='D', color='g')
plt.xticks(fontsize=15)
plt.legend()  # 显示图例

plt.tight_layout()  # 密集显示
plt.show()

# 有时候绘制多张表时需共享一个坐标轴，可以使用sharex='all’命令。
# sharex='all'共享X轴
fig, axs = plt.subplots(4, 1, facecolor='white', figsize=(9, 6), sharex='all')
axs[0].plot(x, y1, label='A', color='r')
axs[1].plot(x, y2, label='B', color='y')
axs[2].plot(x, y3, label='C', color='b')
axs[3].plot(x, y4, label='D', color='g')
plt.show()

# 设置全局变量

# 使用plt.rcParams命令对全局变量设置，包括字符显示、中文显示、背景颜色、标题大小、坐标轴字体大小，线型等。
# 导入模块

# 设置风格
plt.style.use('seaborn-white')

# 设置全局变量
plt.rcParams['axes.unicode_minus'] = False  # 字符显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
plt.rcParams['figure.facecolor'] = 'b'  # 设置图表背景颜色
plt.rcParams['axes.facecolor'] = (0.8, 0.9, 0.8)  # 设置RGB颜色
plt.rcParams['axes.titlesize'] = 20  # 设置标题大小
plt.rcParams['axes.labelsize'] = 20  # 设置轴大小
plt.rcParams['xtick.labelsize'] = 20  # 设置X坐标大小
plt.rcParams['ytick.labelsize'] = 20  # 设置Y坐标大小
plt.rcParams['lines.linestyle'] = '-.'  # 设置线型

plt.plot(x, y1, label='A')
plt.plot(x, y2, label='B')
plt.plot(x, y3, label='C')
plt.plot(x, y4, label='D')
plt.title('折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.legend()  # 显示图例

plt.show()
