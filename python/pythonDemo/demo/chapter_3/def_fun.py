# -*- coding: utf-8 -*-
# 定义函数
# 简略版 只能传入int float类型参数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
# print(my_abs('111')) '>=' not supported between instances of 'str' and 'int'
# 空函数
def nop():
    pass
# 参数检查
def my_abs_plus(x):
    if not isinstance(x, (int, float)):
        # raise TypeError('只能支持 Int or Float类型参数')
        return -1
    if x >= 0:
        return x
    else:
        return -x
# 返回 自定义参数错误值
print(my_abs_plus('10'))
# 多值返回函数
def move(x, y, step):
    nx = x + step
    ny = y - step
    return nx, ny
print(move(10, 20, 5))
# 接收返回值方式
nx, ny = move(10, 20, 5)
# 或者
tupleData = move(10, 20, 5)

print(nx, ny, sep='--')
print(tupleData)
