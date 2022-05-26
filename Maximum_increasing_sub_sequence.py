n = int(input())

list1 = [1,1,2]

if n == 1:
    print(list1[1] % 10007)
elif n == 2:
    print(list1[2] % 10007)
else:
    for _ in range(n-2):
        list1.append((list1[1] + list1[2]))
        list1.pop(0)
        
    print(list1[2] % 10007)