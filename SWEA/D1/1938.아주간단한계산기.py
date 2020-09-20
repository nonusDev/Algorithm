import sys

sys.stdin = open("1938.아주간단한계산기.txt", 'r')

x, y = map(int, input().split())

print(x+y)
print(x-y)
print(x*y)
print(x//y)