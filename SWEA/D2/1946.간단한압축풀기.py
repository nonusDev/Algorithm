import sys

sys.stdin = open("1946.간단한압축풀기.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]