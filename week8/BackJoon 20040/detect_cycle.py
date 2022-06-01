def find_set(set, x):
    if set[x] != x:
        set[x] = find_set(set, set[x])
    return set[x]

def union_set(set, a, b):
    a = find_set(set, a)
    b = find_set(set, b)
    if a < b:
        set[b] = a
    else:
        set[a] = b

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

root = [0] * (n + 1)

edges = []

result = 0

for i in range(1, n + 1):
    root[i] = i
    
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))

cnt = 0

for edge in edges:
    cnt += 1
    a, b = edge
    if find_set(root, a) != find_set(root, b):
        union_set(root, a, b)
    else:
        result = 1
        break

if result == 1:
    print(cnt)
else:
    print(0)
