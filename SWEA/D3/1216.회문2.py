import sys

sys.stdin = open("1216.회문2.txt", 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            