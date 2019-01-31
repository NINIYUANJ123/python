L=[]
for i in range(0,5):
    L.append(input('number:'))
    L[0]=min
    L[4]=max
    for i in range(0,5):
        if(L[i]<min):
            L[0]=L[i]
            if(L[i]>max):
                L[4]=L[i]
                for j in range(0,5):
                    print (L[j])

