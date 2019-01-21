import math
n=float(input("请输入一个数:"))
s=0
for i in range(1,math.floor(n/2)+1):
    if(n%i==0):
        s+=i
if(n==s):
    print("是完数")
else:
    print("不是完数")

