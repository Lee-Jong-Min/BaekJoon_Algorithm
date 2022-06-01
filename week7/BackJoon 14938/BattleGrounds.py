import sys
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]

item = [0] + list(map(int, sys.stdin.readline().split()))

for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

item_cnt = []

for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    cnt = 0
    for j in range(1, n + 1):
        if distance[j] <= m:
            cnt += item[j]
    item_cnt.append(cnt)

print(max(item_cnt))
