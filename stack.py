import sys
stack = [];top1 = -1;test = 1
number_of_test = int(sys.stdin.readline())

while(test<= number_of_test):
    test_case = list(sys.stdin.readline().split())
    if test_case[0] == "push":
        top1 += 1
        if top1 != -1:
            stack.append(test_case[1])
        test += 1
    elif test_case[0] == "pop":
        if top1 == -1:
            print(top1)
        else:
            print(stack.pop())
            top1 -= 1
        test += 1
    elif test_case[0] == "size":
        print(len(stack))
        test += 1
    elif test_case[0] == "empty":
        if top1 == -1:
            print(1)
        else:
            print(0)
        test += 1
    else:
        if top1 == -1:
            print(-1)
        else:
            print(stack[-1])
        test += 1


