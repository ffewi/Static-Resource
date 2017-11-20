# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
list = ['LiLingFeng', 'HanXiChuan', 'YouYongDong']

# >>>['LiLingFeng', 'HanXiChuan', 'YouYongDong']
# list 求长度  len()
len(list)
# >>> 3

# 索引来访问list中每一个位置的元素，记得索引是从0开始的
list[0]
list[1]
list[2]
# >>>'LiLingFeng'
# >>>'HanXiChuan'
# >>>'YouYongDong'

# list[3] 数组越界 list index out of range
# list 使用 -1 取最后一位
list[-1]
# >>>'YouYongDong'
# 使用 -i 逆序取列表 元素，开始从1，也有越界
# 末尾追加元素 .append()
list.append('Liwei')
# 元素插入到指定的位置，比如索引号为1的位置
list.insert(1, 'ZhangWeiWei')
# 删除list末尾的元素，用pop()方法
name = list.pop()
# 删除指定位置的元素，用pop(i)方法，其中i是索引位置 ,小心越界 pop index out of range
name_1 = list.pop(0)
# 某个元素替换成别的元素，可以直接赋值给对应的索引位置
list[0] = list[0] + '_New'
# 很牛逼的是：list里面的元素的数据类型也可以不同
ele = [list, 'Good', 123, True]
# 空的list，它的长度为0
test = len([])
# tuple 有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple = (1, 2, 3)
# 定义只有一个元素的元组，需要注意使用：
t = (1,)
# 不可变的定义，基本数据类型不能变，引用类型引用地址不能变
L1 = [1, 2]
T1 = (88, L1, 99)
# >>>[1, 2]
# >>>(88, [1, 2], 99)
L1.append('APP')
# >>>[1, 2, 'APP']
# >>>(88, [1, 2, 'APP'], 99)
# 多维列表
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
Apple = L[0][0]
Python = L[1][1]
Lisa = L[2][2]
print(L[0][0], L[1][1], L[2][2])
print(L1, T1, sep='\n')
# print(tuple)
