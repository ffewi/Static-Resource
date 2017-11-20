# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print('包含中文的str')
ord('A')
# >>>65
ord('中')
# >>>20013
chr(66)
# >>>B
chr(25991)
# >>>文
print('\u4e2d\u6587')
# >>>中文

# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
# 编码 --> 字节
'ABC'.encode('ascii')
# >>>b'ABC'
'中文'.encode('utf-8')
# >>>b'\xe4\xb8\xad\xe6\x96\x87'
# 解码 --> 字符
b'ABC'.decode('ascii')
# >>>'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# >>>'中文'

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# >>>'中

# 计算str包含多少个字符，可以用len()函数
len('ABC')
# >>>3
len('中文')
# >>>2

# len()函数就计算字节数
len(b'ABC')
# >>>3
len(b'\xe4\xb8\xad\xe6\x96\x87')
# >>>6
len('中文'.encode('utf-8'))
# >>>6

# 按照UTF-8编码读取源代码
# --> #!/usr/bin/env python3 <--
# --> # -*- coding: utf-8 -*- <--

# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?
# 占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

'Age: %s. Gender: %s' % (25, True)
# >>>'Age: 25. Gender: True'
'growth rate: %d %%' % 7
# >>>'growth rate: 7 %'
# format()函数
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# >>>'Hello, 小明, 成绩提升了 17.1%'
i1 = int(input('in:'))
print(i1)
