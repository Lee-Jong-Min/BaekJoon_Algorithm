def change(A,B,i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0


N,M= map(int,input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int,input())))

for _ in range(N):
    B.append(list(map(int,input())))

count = 0

if (N < 3 or M < 3) and A != B:
    count = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                change(A,B,i,j)
                count += 1

if count != -1:
    if A != B:
        count = -1

print(count)
    
