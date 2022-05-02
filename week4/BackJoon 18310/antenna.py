import sys

num_of_house = int(sys.stdin.readline())

house = list(map(int,sys.stdin.readline().split()))

house.sort()

if num_of_house % 2 == 0:
    print(house[int(num_of_house/2)-1])
elif num_of_house % 2 == 1:
    print(house[int(num_of_house/2)])
