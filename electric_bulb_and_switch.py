N = int(input())
electric_bulb1 = list(map(int,input()))
electric_bulb2 = list(map(int,input()))

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

def switch(bulb1,bulb2,state):
    count = state
    if count == 1:
        bulb1[0] = change(bulb1[0])
        bulb1[1] = change(bulb1[1])
    for i in range(1,N):
        if bulb1[i-1] != bulb2[i-1]:
            count += 1
            bulb1[i-1] = change(bulb1[i-1])
            bulb1[i] = change(bulb1[i])
            if i != N-1:
                bulb1[i+1] = change(bulb1[i+1])
    if bulb1 == bulb2:
        return count
    else:
        return -1

res1 = switch(electric_bulb1[:],electric_bulb2[:],0)
res2 = switch(electric_bulb1[:],electric_bulb2[:],1)

if res1 >= 0 and res2 >= 0:
    print(min(res1,res2))
elif res1 >= 0 and res2 <= 0:
    print(res1)
elif res1 <= 0 and res2 >= 0:
    print(res2)
else:
    print(-1)