def k(score):
    if score > 90:
        return 'A'
    elif score > 60:
        return 'B'
    else:
        return 'C'
score = int(input('输入分数:\n'))
level = k(score)
print('Level is :',level)

