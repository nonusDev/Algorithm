import sys

sys.stdin = open("1284.수도요금전쟁.txt", 'r')

for tc in range(1, int(input())+1):
    P, Q, R, S, W = map(int, input().split())

    x = P * W
    if W <= R:
        y = Q
    else:
        y = Q + ((W-R) * S)
    
    print(f"#{tc} {min(x, y)}")