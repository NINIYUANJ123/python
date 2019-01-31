def people (x):
    if x == 1:
        return 10
    else:
        return people(x-1) + 2
print(people(5) )
