# 函数的参数
def power(x):
    return x * x
# 调用函数
power(5)
# >>>25
# TypeError: power() takes 1 positional argument but 2 were given
# power(5, 2)
# 计算 x的n次方
def power_plus(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
v = power_plus(5, 3)
print(v)
# TypeError: power() missing 1 required positional argument: 'n'
# power_plus(5)

# 带默认参数值的函数 默认参数必须指向不可变量
def power_by_default_val(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
v1 = power_by_default_val(5, 3)
v2 = power_by_default_val(5)
print(v1, v2, sep=' -- ')
# 为什么 默认参数必须指向不可变量 测试：
def add_end(L=[]):
    if L is None:
        L = []
    L.append('END')
    return L
# ['END']
print(add_end())
# ['END', 'END']
print(add_end())

# 可以看出 当默认参数为引用变量时， 往往最终的数据结构会出乎意料

# 改良版 ，不管怎么调用，只返回一种情况
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# ['END']
print(add_end())
print(add_end())

# 可变参数 求平方和 弊端，必须以集合方式传入 list tuple dict set
def varArgs(vars):
    sum = 0
    for n in vars:
        sum = sum + n * n
    return sum
# 以集合列表方式传参数
print(varArgs((1,2,3)))

# 改良可变参数
def varArgs_plus(*vars):
    sum = 0
    for n in vars:
        sum = sum + n * n
    return sum
# 可变参数个数 传参
print(varArgs_plus(1,2,3))
## 关键字 参数 关键字参数在函数内部自动组装为一个dict
def position(name, age, **kw):
    d = {}
    if 'student' in kw:
        # 有city参数
        d['student'] = kw['student']
    if 'worker' in kw:
        # 有job参数
        d['worker'] = kw['worker']
    print(name, age, d, sep=' -- ')
position('liwei', 24, student=True)
position('liwei', 24, worker=True)
position('liwei', 24, student=True, worker=True)
d = {'student': True, 'worker': True}
position('liwei', 24, **d)