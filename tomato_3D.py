def bfs():
    
    cnt = 0
    
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x,y,z = queue.popleft()
            
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                    continue
                if graph[nz][nx][ny] == 0:
                    queue.append((nx,ny,nz))
                    graph[nz][nx][ny] = 1
                if graph[z][x][y] == -1:
                    continue
    return cnt-1

import sys
from collections import deque

M,N,H = map(int,sys.stdin.readline().split())
graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if graph[k][i][j] == 1:
                queue.append((i,j,k))

a = bfs()
flag = 1
if a == 0:
    print(0)
else:
    for i in graph:
        if flag == 1:
            for j in i:
                if 0 in j:
                    print(-1)
                    flag = 0
                    break
        else:
            break
    if flag == 1:
        print(a)
