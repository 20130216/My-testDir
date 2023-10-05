# 导入pandas库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 生成一个Series
s = pd.Series([1, 3, 3, 4], index=list('ABCD'))

# 括号内不指定图表类型，则默认生成直线图
s.plot()
print("直线图")
plt.show()

# 条形图
s.plot(kind='bar')
print("条形图")
plt.show()

# 水平条形图
s.plot.barh()
print("水平条形图")
plt.show()

# 饼图
s.plot.pie()
print("饼图")
plt.show()

# 直方图
s.plot.hist()
print("直方图")
plt.show()

# 密度图

s = pd.Series(np.random.randn(1000))  # 生成一列随机数
s.plot.kde()
s.plot.density()

print("密度图")
plt.show()

# 散点图
# 生成一个DataFrame
df = pd.DataFrame(np.random.randn(1000, 2),
                  columns=['X1', 'Y'])
df.plot.scatter(x='X1', y='Y')

print("散点图")
plt.show()

# 六角箱图
df.plot.hexbin(x='X1', y='Y', gridsize=8)
print("六角箱图")
plt.show()

# 箱型图
df = pd.DataFrame(np.random.rand(10, 2), columns=['A', 'B'])
df.plot.box()
print("箱型图")
plt.show()

# 面积图
df = pd.DataFrame(np.random.randint(10, size=(4, 4)),
                  columns=list('ABCD'),
                  index=list('WXYZ'))

df.plot.area()
print("面积图")
plt.show()
