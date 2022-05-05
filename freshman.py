import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    cnt = 1
    score = []
    N = int(sys.stdin.readline())
    
    for j in range(N):
        score.append(tuple(map(int,sys.stdin.readline().split())))

    score.sort(key = lambda x : x[0])
    score1 = score[0][1]
    
    for k in score:
        if(score1 > k[1]):
            cnt += 1
            score1 = k[1]
            
    print(cnt)