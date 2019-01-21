InPut = input('请输入字符串：')
letters  = [ ]
spaces = [ ]
digits   = [ ]
others = [ ]
for i in iter(InPut):
    if i.isalpha():
        letters.append(i)
    elif i.isspace():
        spaces.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        others.append(i)
print('中英文字母个数：%s' % len(letters))
print('空格个数：%s' % len(spaces))
print('数字个数：%s' % len(digits))
print('其它字符个数：%s' % len(others))
