n=int(input())

M=list(map(int, str(n)))
M=sorted(M, reverse=True)
for x in M:
    print(x, end='')