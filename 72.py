str1 = input('请输入:\n')
str2 = input('请输入:\n')
str3 = input('请输入:\n')
if str1 > str2 : str1,str2 = str2,str1
if str1 > str3 : str1,str3 = str3,str1
if str2 > str3 : str2,str3 = str3,str2
print (str1,str2,str3)
