# 循环
names = ['Xiao', 'Kaka', 'Aqu']
# for 的用法
#
for name in names:
    print(name)
# rang() 函数
# range(start, stop = None, step);
r = range(6)
print(list(r))

# while 循环
# 求奇数的和
sum = 0
n = 99
sumList = []
while n > 0:
    sum = sum + n
    sumList.append(n)
    n = n - 2
print(sum)
print(sumList)

# 生成 1-99 的奇数列表
L1 = list(range(1, 100, 2))
print(L1)

# 循环时 使用break 中断循环
# 使用 continue 跳过本次循环，继续下次循环
n = 1
while n <= 100:
    # 当n = 9时，条件满足，执行break语句
    if n > 8:
        # break语句会结束当前循环
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    # 如果n是偶数，执行continue语句
    if n % 2 == 0:
        # continue语句会直接继续下一轮循环，后续的print()语句不会执行
        continue
    print(n)
