arr1 = [0,1,1]
arr2 = [1,0,1]

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    length = len(arr1)
    if length <= N:
        for i in range(length,N+1):
            arr1.append(arr1[i-1] + arr1[i-2])
            arr2.append(arr2[i-1] + arr2[i-2])
        print(arr2[N],arr1[N])
    else:
        print(arr2[N],arr1[N])
    
