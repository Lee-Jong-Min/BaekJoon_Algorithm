import sys
import heapq as hq

N = int(input())
lecture = []
for i in range(N):
    S,T = map(int,sys.stdin.readline().split())
    lecture.append((S,T))

lecture.sort(key = lambda x: x[0])

classroom = []
hq.heappush(classroom,lecture[0][1])

for i in range(1,N):
    if(lecture[i][0] < classroom[0]):
        hq.heappush(classroom,lecture[i][1])
    else:
        hq.heappop(classroom)
        hq.heappush(classroom,lecture[i][1])
print(len(classroom))