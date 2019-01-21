a=[1,2,3,4,2,6,4,6,7,5,3]
b=set(a)
for each_b in b:
    count=0
    for each_a in a:
        if each_b == each_a:
            count+=1
    print(each_b,":",count)
