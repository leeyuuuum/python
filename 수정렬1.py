n=int(input())
L=[]
for x in range(n) :
    a=(int(input()))
    L.append(a)

L.sort()
for x in L:
    print(x)