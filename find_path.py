import sys

INF = int(1e9)

n = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n + 1):
        graph[i][j] = data[j - 1]
           
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1
                    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()