lst = []
for i in range(100):
    lst.append(101+i)
 
for i in range(101, 201):
    for j in range(2,i):
        if i%j == 0:  
            lst.remove(i)  
            break
print(lst)
