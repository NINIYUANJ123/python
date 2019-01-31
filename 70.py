def two(n):
    m=0
    sum=0
    for i in range(2,n+2,2):
        m=1.0/i
        sum=sum+m
        return sum
def one(n):
    m=0
    sum=0
    for i in range(2,n+2,2):
        m=1.0/(i+1)
        sum=sum+m
        return sum
if __name__ == '__main__':
    n=int(input('n:\n'))
    if n%2==0:
        s=two(n)
    else:
        s=one(n)
    print (s)
