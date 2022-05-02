import sys
import bisect

test_case = int(input())

for i in range(test_case):
    cnt = 0
    N,M = map(int,sys.stdin.readline().split())
    A = list(map(int,sys.stdin.readline().split()))
    B = list(map(int,sys.stdin.readline().split()))
    
    A.sort()
    B.sort()
    
    for j in B:
        a = bisect.bisect_right(A,j)
        cnt += (len(A) - a)
    print(cnt)
    