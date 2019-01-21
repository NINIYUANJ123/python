for i in range(0,5):
    for y in range(0,5-i):
        w = ' '
        print(w,end="")
    s = '* ' * i
    print(s)
for i in range(0,5):
    for x in range(0,i):
        w = ' '
        print(w, end="")
    t = '* ' * (5-i)
    print(t)
