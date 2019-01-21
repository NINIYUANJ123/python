a=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
year=int(input("请输入需要判断的年："))
month = int(input("请输入需要判断的月："))
day = int(input("请输入需要判断的日："))
sum=0
if (year%4==0 and year%100!=0)or year%400==0:
    for i in range(1,month):
            sum=sum+a[1][i]
else:
    for i in range(1,month):
            sum=sum+a[0][i]
sum=sum+day
print("%d"%sum)
