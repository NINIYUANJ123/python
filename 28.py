sum = 0
a, b = 2, 1
for i in range(20):
    sum = sum + a/b
    a = a + b
    b = a - b
print(sum)
