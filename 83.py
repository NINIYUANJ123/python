filename = input("输入文件名:")
fp = open(filename, "w")
character = input("输入字符串:")
while character != '#':
    fp.write(character)
    character = input("输入字符串:")
fp.close()
print('\n')
