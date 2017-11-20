# 数据类型和变量
#
#
# 整型
v1 = 1
# 浮点型
v2 = 0.01
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
v3 = 'I\'m \"OK\"!'
# 转义符
v4 = '\\\t\\'
# Python还允许用r''表示''内部的字符串默认不转义
v5 = r'\\\t\\'
# Python允许用'''...'''的格式表示多行内容
v6 = '''第一句
... 第二句
... 第三句'''
# 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，
# 在Python中，可以直接用True、False表示布尔值（请注意大小写）
v7 = True
v8 = False
# and运算是与运算，只有所有都为True，and运算结果才是True
v9 = True and True
v10 = True and False
v11 = False and False
v12 = 15 > 3 and 13 > 1
# or运算是或运算，只要其中有一个为True，or运算结果就是True
v13 = True or True
v14 = True or False
v15 = False or False
v16 = 15 > 3 or 13 > 1
# not运算是非运算，它是一个单目运算符，把True变成False，False变成True
v17 = True or True
v18 = True or False
v19 = False or False
v20 = 15 > 3 or 13 > 1
# 条件判断
# age = input('请输入您的年龄：')
print('比较值')
age = 22
if age >= 18:
    print('adult')
else:
    print('teenager')
print(v1, v2, v3, v4, v5, v6, v7, v8, sep='\n', end='\n')
# a是整数
a = 123
print(a)
# a变为字符串
a = 'ABC'
print(a)
# ++
x = 10
x = x + 2

print(x)
# 字符值 传递
a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a)

# 精确除法 / 向下取整 // 取余数 %
m1 = 10 / 3
m2 = 10 // 3
m3 = 10 % 3
print(m1, m2, m3, sep='\n')

s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(s3, s4, sep='\n')
