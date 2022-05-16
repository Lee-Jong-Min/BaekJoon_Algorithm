def bfs(ng):
    q = collections.deque([])
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    global max_num
    
    for virus in virus_list:
        q.append(virus)
        
    while q:
        cy,cx = q.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if ng[ny][nx] == empty and visited[ny][nx] == False:
                q.append([ny,nx])
                ng[ny][nx] = virus
                visited[ny][nx] = True
        
    for i in range(n):
        cnt += ng[i].count(empty)
            
    if max_num < cnt:
        max_num = cnt

import sys,copy,collections

n,m = map(int,sys.stdin.readline().split())

max_num = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

empty_list = []
virus_list = []

empty = 0
wall = 1
virus = 2

g = [[0]*m for _ in range(n)]

for y in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]
    
    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == empty:
            empty_list.append([y,x])
        if g[y][x] == virus:
            virus_list.append([y,x])
            
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1,x1 = empty_list[i]
            y2,x2 = empty_list[j]
            y3,x3 = empty_list[k]
            
            g[y1][x1] = wall
            g[y2][x2] = wall
            g[y3][x3] = wall
            
            ng = copy.deepcopy(g)
            bfs(ng)
            
            g[y1][x1] = empty
            g[y2][x2] = empty
            g[y3][x3] = empty
            
print(max_num)