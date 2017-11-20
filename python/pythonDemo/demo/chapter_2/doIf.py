# 条件判断

# 简单的判断
money = 2000
if money >= 2000:
    print('有一笔钱： %d' % money)
    print('初试小刀')

# 双流程
name = 'Liwei'
if name == 'Liwei':
    print('老大：%s' % name)
    print('欢迎老大回家！')
else:
    print('贼人：%s' % name)
    print('小的，抓起来烧烤！')
# 条件判断标准格式
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = [1, 2]
if not x:
    print('x 是零数值、空字符串、空list')
else:
    print('x: %s' % x)
    pass
