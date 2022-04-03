import sys

N,K = map(int,input().split())
value = 0; min = 0
A = []


for j in range(N):
    A.append(int(sys.stdin.readline()))
    
for i in range(N-1,-1,-1):
    temp = divmod(K,A[i])
    value += temp[0]
    K = temp[1]
    
print(value)


