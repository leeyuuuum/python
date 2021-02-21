#n은 홀수라고 가정
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys
from collections import Counter

n=int(input())

L=[]
T=[]

for x in range(n):
    L.append(int(sys.stdin.readline()))

#산술평균
san = round(sum(L) / n)

#중앙값
M=sorted(L)
mid = M[n//2]

#최빈값
cnt=Counter(M)
mode=cnt.most_common()

if n==1:
    mode = mode[0][0]
    
else :
    if mode[0][1] == mode[1][1]:
        mode = mode[1][0]
    else:
        mode = mode[0][0]


#범위
ran=max(L)-min(L)


print(san)
print(mid)
print(mode)
print(ran)