l=[]
n=int(input("请输入数字n:"))
for i in range(2,(n+1)):
    a=0
    for j in range(2,i):
        if(i%j==0):
            a=1
    if (a==0):
        l.append(i)
print(len(l))
