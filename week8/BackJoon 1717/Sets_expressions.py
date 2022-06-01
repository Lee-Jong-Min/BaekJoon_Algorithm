def union_set(set, a, b):
    a = find_set(set, a)
    b = find_set(set, b)
    if a < b:
        set[b] = a
    else:
        set[a] = b
        
def find_set(set, x):
    if set[x] != x:
        set[x] = find_set(set, set[x])
    return set[x]

import sys
sys.setrecursionlimit(10**6)

a, b = map(int, sys.stdin.readline().split())

root = [0] * (a + 1)

for i in range(a + 1):
    root[i] = i

for _ in range(b):
    c, d, f = map(int, sys.stdin.readline().split())
    if c == 0:
        union_set(root, d, f)
    elif c == 1:
        if find_set(root, d) == find_set(root, f):
            print("YES")
        else:
            print("NO")
