a= [4,5,7,10,13,19,20,27,37,99,109]
print ('原始数据:')
for i in range(len(a)):
    print (a[i])
number = int(input("新数字是:\n"))
end = a[9]
if number > end:
    a[10] = number
else:
    for i in range(10):
        if a[i] > number:
            temp1 = a[i]
            a[i] = number
            for j in range(i + 1,11):
                temp2 = a[j]
                a[j] = temp1
                temp1 = temp2
            break
for i in range(11):
    print (a[i])
