import sys
import heapq

test_case = int(sys.stdin.readline())
heap = []

for i in range(test_case):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(heap,num)
    elif len(heap) != 0:
        print(heapq.heappop(heap))
    else:
        print(0)