# 条件判断语句

import math
a = 5

if a > 0:
    print("a是正数")
else:
    print("a是负数或0")

# 循环语句

i = 0

while i < 5:

    print(i)
    i += 1
# 遍历列表

words = ["hello", "wei", "!"]

for word in words:

    print(word)

# 函数定义


def add(a, b):
    c = a + b
    return c

# 函数调用


result = add(1, 2)

print(result)
# 导入模块
# 使用模块

x = math.cos(45)

print(x)

# 文件读写操作

# 写入文件

f = open("test.txt", "w")
f.write("test")

f.close()

# 读取文件

f = open("test.txt", "r")

x = f.read()

print(x)

f.close()

# csdn引用链接
# https://blog.csdn.net/weixin_49895216/article/details/132356263
