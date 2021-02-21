# import sys
# max_num = 10000

# n=int(input())
# L=[]
# for x in range(n) :
#     #L.append(int(input()))
#     L.append(int(sys.stdin.readline()))

# count = [0] * (max_num+1) #[0, 0, 0, 0, ...] max_num+1개 만큼의 0이 list에 들어감
# countsum = [0] * (max_num+1)

# for i in range(n) :
#     count[L[i]] +=1

# countsum[0] = count[0]

# for i in range(1, max_num+1):
#     countsum[i] = countsum[i-1] + count[i]

# array = [0] * (n+1)

# for i in range(n-1, -1, -1):
#     array[countsum[L[i]]] = L[i]
#     countsum[L[i]] -=1
#     #print(array)
#     #print("\n")

# for i in array[1:]:
#     print(i)


import sys
n=int(input())
count=[0]*10001

for x in range(n):
    num = int(sys.stdin.readline())

    count[num] +=1

for i in range(10001):
    if count[i] !=0:
        for j in range(count[i]):
            print(i)