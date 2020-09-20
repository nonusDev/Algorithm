import sys

sys.stdin = open("1936.1대1가위바위보.txt", 'r')

x, y = map(int, input().split())

if x-y == 1 or x-y == -2:
    print('A')
else:
    print('B')