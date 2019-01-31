a=int(input("请输入三个数字:"))
b=int(input("请输入三个数字:"))
c=int(input("请输入三个数字:"))
if a>b:
    j=a
    a=b
    b=j
if a>c:
    j=a
    a=c
    c=j
if b>c:
    j=b
    b=c
    c=j
print("%d %d %d"%(a,b,c))
