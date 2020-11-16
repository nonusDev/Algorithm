import sys

sys.stdin = open("1217.거듭제곱.txt", 'r')

def power(x, y, res):
    if y == 0:
        return f"#{tc} {res}"
    res *= x
    return power(x, y-1, res)

T = 10
for t in range(1, T+1):
    tc = int(input())
    N, M = map(int, input().split())
    
    print(power(N, M, 1))