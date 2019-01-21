a = int(input('请输入数字a：'))
number = int(input('请输入几个数相加：'))
sum = 0
for i in range(1, number + 1):
    t = 0
    for j in range(i):
        t = t + 10 ** j
    sum +=a*t
print(sum)
