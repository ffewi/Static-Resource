# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {"name": "liwei", "age": 24, "habbit": "IT"}
print(d['name'])
# 修改dict 的值
d['name'] = 'new_name'
print(d)
# 取值时没有key 会报错
# KeyError: 'error'
# d['error']
# 解决 KeyError 可以先判断 有没有这个key
print('error' in d)
# 方法二 通过 get方式 没有 返回None ，或者指定默认返回值
print(d.get('error'))
print(d.get('error', 'not found!'))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('age')
print(d)

# set，是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 会自动将重复数据过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
# 第二次重复数据不会再添加进去
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素 ,如果没有值 会报出 KeyError ,同样可以使用 in 方法 判断是否存在key
if 4 in s:
    s.remove(4)
    pass
# !!! set集合 可以做交 、并、异或运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
# {2, 3}
# {1, 2, 3, 4}
# {1, 4}
nerStr = 'abcaa'.replace('a', 'A', 1)
print(nerStr)
