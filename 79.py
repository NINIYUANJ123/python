n = 0
while n < 7:
    number = int(input("请输入一个整数:"))
    for _ in range(number):
        print('*', end='')
    n += 1
    print('\n')
