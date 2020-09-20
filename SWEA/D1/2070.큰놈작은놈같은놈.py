import sys

sys.stdin = open("2070.큰놈작은놈같은놈.txt", 'r')

for tc in range(1, int(input())+1):
    x, y = map(int, input().split())

    if x > y:
        res = '>'
    elif x == y:
        res = '='
    else:
        res = '<'
    
    print(f"#{tc} {res}")