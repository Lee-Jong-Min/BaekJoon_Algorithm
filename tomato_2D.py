def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    cnt = 0
    
    while queue:
        x,y = queue.popleft()
        l = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            elif graph[nx][ny] == 0:
                queue.append((nx,ny))
                if graph[x][y] == 1:
                    graph[nx][ny] = 1
                    if l == 1:
                        cnt += 1
                elif graph[x][y] == -1:
                    continue
            elif graph[nx][ny] == 1:
                continue
            
    return cnt

import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())

graph = []

for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            start_x,start_y = i,j

a = bfs(start_x,start_y)
b = 1
if a == 0:
    print(0)
else:
    for i in range(N):
        if graph[i].count(0) != 0:
            print(-1)
            b = 0
            break
    if b == 1:
        print(a)