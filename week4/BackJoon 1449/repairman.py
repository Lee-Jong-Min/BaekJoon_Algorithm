N,L = map(int,input().split())
loc = list(map(int,input().split()))

loc.sort()
cnt = 0

for i in loc:
    if i == loc[0]:
        start = i
        end = start + L - 0.5
        cnt += 1
    else:
        if start <= i < end:
            continue
        else:
            start = i
            end = start + L - 0.5
            cnt += 1

print(cnt)
