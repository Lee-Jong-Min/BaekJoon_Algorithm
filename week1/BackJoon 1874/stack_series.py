test_case = int(input())
stack = []
operation = []
index = 1
flag = 0

for i in range(test_case):
    num = int(input())
    while index <= num:
        stack.append(index)
        operation.append("+")
        index += 1
    if stack[-1] == num:
        stack.pop()
        operation.append("-")
    else:
        flag = 1

if flag == 0:
    for i in operation:
        print(i)
else:
    print("NO")
