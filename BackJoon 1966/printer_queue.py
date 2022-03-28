test_case = int(input())

for _ in range(test_case):
    n,m = list(map(int,input().split()))
    importance = list(map(int,input().split()))
    index = m
    number_of_print = 0

    while True:
        if importance[0] == max(importance):
            number_of_print += 1
            if index == 0:
                print(number_of_print)
                break
            else:
                importance.pop(0)
                index = index - 1
        else:
            importance.append(importance.pop(0))
            if index == 0:
                index = len(importance) - 1
            else:
                index = index - 1
