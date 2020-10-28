import sys

sys.stdin = open("3431.준환이의운동관리.txt", 'r')

for tc in range(1, int(input())+1):
    L, U, X = map(int, input().split())
    print(L)