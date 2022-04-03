N = int(input())
temp = list(map(int,input().split()))
P = sorted(temp)
sum = 0
min = 0

for i in range(N):
    for j in range(i+1):
        sum += P[j]
    min += sum
    sum = 0

print(min)