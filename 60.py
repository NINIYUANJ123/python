x=int(input('请输入数:'))
if x>0:
    x=str(x)
    new=''
    for i in range(len(x)-1,-1,-1):
        new=new+x[i]
    new=int(new)
    if new>=2**31-1:
        new=0
    print(new)
else:
    x=str(-x)
    new = ''
    for i in range(len(x) - 1, -1, -1):
        new = new + x[i]
    new=int(new)
    new=-new
    if new<=-2**31:
        new=0
    print(new)
