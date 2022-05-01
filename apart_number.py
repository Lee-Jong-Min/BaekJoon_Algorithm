def dfs(x,y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
result = 0
num_apart = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i,j) == True:
            num_apart.append(cnt)
            result += 1

num_apart.sort()
print(result)
for i in num_apart:
    print(i)