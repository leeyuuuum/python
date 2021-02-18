n=int(input())
W=[]
for x in range(n):
    w, h = input().split()
    W.append((int(w), int(h)))

for x in W:
    rank =1
    
    for y in W:
        if x[0] < y[0] and x[1] < y[1]:
            rank +=1
    print(rank, end=' ')