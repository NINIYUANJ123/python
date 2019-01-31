fp1 = open("text1.txt", "w+")
fp1.write('123')
fp1.close()

fp2 = open("text2.txt", "w+")
fp2.write('456')
fp2.close()

fp1 = open("text1.txt", "r")
a = fp1.read()
fp1.close()

fp2 = open("text2.txt", "r")
b = fp2.read()
fp2.close()

l = list(a + b)
l.sort()
s = ''
s = s.join(l)
fp = open("test3.txt", "w+")
fp.write(s)
fp.close()
