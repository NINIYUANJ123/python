count=0
for i in range(100,201):
    for x in range(100,i):
        if i%x==0:
            break
        else:
            count+=1
    print("%d"%i)
            
