def triangles(max):
    L = [1]
    for i in range(1,max+1):
        yield(L)
        L.append(0)
        L = [L[x]+L[x-1] for x in range(1,i)]
        L.insert(0,1)
        L.append(1) 
for i in triangles(5):
    print(i)
