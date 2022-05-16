test_case = int(input())

for _ in range(test_case):
    arry = [1,1,1]
    N = int(input())
    if(len(arry) <= N):
        for i in range(len(arry),N):
            arry.append(arry[i-3]+arry[i-2])
        print(arry[N-1])
    else:
        print(arry[N-1])
