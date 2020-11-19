import sys
from collections import deque

sys.stdin = open("1225.암호생성기.txt", 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = deque(list(map(int, input().split())))

    cnt = 1
    while True:
        tmp = arr.popleft()
        if tmp - cnt <= 0:
            arr.append(0)
            break
        else:
            arr.append(tmp - cnt)
        cnt += 1
        if cnt > 5:
            cnt = 1

    print(f"#{tc}", end=' ')
    print(*arr)