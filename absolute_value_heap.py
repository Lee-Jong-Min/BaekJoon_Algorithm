import sys
import heapq

test_case = int(sys.stdin.readline())
heap = []

for i in range(test_case):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,(abs(num),num))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
        