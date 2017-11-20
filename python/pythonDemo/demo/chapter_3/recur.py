# -*- coding: utf-8 -*-
# 递归函数
# 带函数表达式的递归，量大了会出现 递归调用的次数过多，会导致栈溢出
def recur1(n):
    if n == 1:
        return 1
    return n * recur1(n - 1)
v1 = recur1(5)
# RecursionError: maximum recursion depth exceeded in comparison
# v1 = recur1(1000)
print(v1)

# 解决递归调用栈溢出的方法是通过尾递归优化
def recur2(n, result):
    if n <= 1:
        return result
    return recur2(n - 1, n * result)
v2 = recur2(5, 1)
print(v2)
# v3 = recur2(100, 1)
# print(v3)

# 将b看作临时作用，步骤1：需要把n-1块A上面的移动到B，将A移动到C，
# 剩下步骤将B的n-1块移动到C（此时可以将A看作临时作用）
def haNorTa(n, a, b, c):
    if n <= 1:
        print(a, '-->', c)
        return
    else :
        haNorTa(n - 1, a, c, b)
        haNorTa(1, a, b, c)
        haNorTa(n - 1, b, a, c)

haNorTa(5, 'A', 'B', 'C')