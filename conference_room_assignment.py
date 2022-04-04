import sys

N = int(input())
conference_time = []
for i in range(N):
    ST,FT = map(int,sys.stdin.readline().split())
    conference_time.append((ST,FT))
    
conference_time.sort(key = lambda x: (x[1],x[0]))

end_time = 0
conference = []

for i in conference_time:
    if i[0] >= end_time:
        conference.append(i)
        end_time = i[1]
print(len(conference))
