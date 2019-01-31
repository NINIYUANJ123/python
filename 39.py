for i in range(2,101):
    flag=0
    for g in range(2,i):
        if(i%g==0):
            flag=1
    if(flag==0):
        print("%d"%i)
            
            
