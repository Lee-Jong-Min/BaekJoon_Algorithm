def bfs():
    
    cnt = 0
    
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                    graph[nx][ny] = 1
                if graph[x][y] == -1:
                    continue
    return cnt-1

import sys
from collections import deque
M,N = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
    
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))

a = bfs()
flag = 1

if a == 0:
    print(0)
else:
    for i in graph:
        if 0 in i:
            print(-1)
            flag = 0
            break
    if flag == 1:
        print(a)
