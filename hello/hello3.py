# python保留字
import keyword
keyword.kwlist
# [‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
# 4、注释和空行
# 单行注释：#
# 多行注释：多行注释可以用多个 # 号，还有 ‘’’ 和 “”"：
# 无需； 用空行隔断语句，若一行需要多条语句则用；隔开
#!/usr/bin/python3
print("Over")

# 行与缩进
if 0:
    print("xx")
else:
    print("yy")  # 输出的是yy

xiaobin = 1
print(xiaobin)  # 输出 1

# 声明变量
# 等号（=）赋值
# 多变量赋值如下：
a = b = c = 1  # a = 1;b = 1; c = 1
a, b, c = 1, 2, "ranxia"  # a = 1;b = 2; c =“ranxia”
print(c)

# 8.1 Number（数字）
# 内置的 type() 函数和 isinstance() 可以用来查询变量所指的对象类型。
ranxia = 228  # 当变量被赋值时，Number对象即被创建
print(type(ranxia))  # <class ‘int’>
print(isinstance(ranxia, int))  # True

# 数值运算：

print(1 + 1)  # 加法 2
print(5.2 - 2)  # 减法 3.2
print(3 * 7)  # 乘法 21
print(2 / 4)  # 除法，取浮点数0.5
print(2 // 4)  # 除法，取整数 0
print(5 % 2)  # 取余 1
print(2 ** 3)  # 乘方，8

# 8.2 字符串(str1ing)
word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以由多行组成"""
print(word)  # 字符串
print(sentence)  # 这是一个句子。
print(paragraph)  # 这是一个段落，

# 可以由多行组成
print("xiao’bin’")  # xiao’bin’
print("aaaaaaaaaa"
      "11111")  # aaaaaaaaaa11111
print("this is a line \n next line ")
print(r"this is a line next line \n")  # r不发生转义

str1 = "ranxia"
print(str1)  # ranxia
print(str1[0:-1])  # ranxi
print(str1[0])  # r
print(str1[2:5])  # nxi
print(str1[2:])  # nxia
print(str1 * 2)  # ranxiaranxia *表重复
print(str1 + ' 你好！')  # ranxia你好 +号表连接
print('ran\nxia')  # ran

print("我喜欢%s已经%d年了" % ("冉冉", 16))  # 我喜欢冉冉已经16年了
print("我喜欢{}已经{}年了".format("冉冉", 16))  # 我喜欢冉冉已经16年了
print("我喜欢{1}已经{0}年了".format(16, "冉冉"))  # 我喜欢冉冉已经16年了 #这种方式可以指定顺序

# 8.4 Tuple（元组）
tuple1 = ('Google', 'Runoob', 'Taobao')
leng = len(tuple1)
print(' 该行拥有的单词数是：'+str(leng))

# 8.6 Dictionary（字典）

# 14、迭代器与生成器

list = [5, 6, 7, 8]
it = iter(list)
for x in it:
    print(x, end=" ")  # 5 6 7 8

print("\n")

# 14.2 生成器


def yield_test():
    print("开始…")
    yield "hello ranxia"
    print("测试")


test = yield_test()
print(next(test))  # 开始.. hello ranxia
# print(next(test))  # 测试  这个放出来会出错

# 15、函数


def test(var):
    if var == "ranxia":
        print("love u")
    else:
        print("piss off")


test("ranxia")

# 引用链接csdn
# https://blog.csdn.net/weixin_49895216/article/details/132995458?spm=1001.2014.3001.5501
