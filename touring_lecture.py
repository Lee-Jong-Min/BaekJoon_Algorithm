import sys
import heapq as hq


n = int(input())
pay = []

for i in range(n):
    p,d = map(int,sys.stdin.readline().split())
    pay.append((p,d))

pay.sort(key = lambda x: x[1])
heap = []

for i in pay:
    hq.heappush(heap,i[0])
    if(len(heap) > i[1]):
        hq.heappop(heap)

print(sum(heap))