import sys

sys.stdin = open("2029.몫과나머지출력하기.txt", 'r')

for tc in range(1, int(input())+1):
    x, y = map(int, input().split())

    print(f"#{tc} {x//y} {x%y}")