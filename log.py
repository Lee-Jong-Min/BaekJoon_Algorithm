import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    N = int(sys.stdin.readline())
    L = list(map(int,sys.stdin.readline().split()))
    L.sort(reverse = True)

    level = []

    for i in range(N):
        if i == 0:
            level.append(abs(L[i] - L[i+1]))
            level.append(abs(L[i] - L[i+2]))
        else:
            if i == N-2:
                level.append(abs(L[i] - L[i+1]))
            else:
                if i != N-1:
                    level.append(abs(L[i] - L[i+2]))
                else:
                    pass
    print(max(level))
    