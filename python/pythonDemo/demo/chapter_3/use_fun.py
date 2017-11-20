# 调用函数
# help(abs)
# help(ord)
v1 = abs(-1)
# max(iterable, default, key)
v2 = max([1, 2, 3])
# Python内置的常用函数还包括数据类型转换函数
int('123')
# >>>123
int(12.34)
# >>>12
float('12.34')
# >>>12.34
str(1.23)
# >>>'1.23'
str(100)
# >>>'100'
bool(1)
# >>>True
bool('')
# >>>False
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
# 变量a指向abs函数
a = abs
# 所以也可以通过a调用abs函数
a(-1)
# >>>1
print(v1, v2, sep='\n')
print(bool('hello'), bool([]))
# hex() 转换为十六进制
hex(12648430)
