import sys

sys.stdin = open("1961.숫자배열회전.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [map(int, input().split()) for _ in range(N)]

    arr_1 = list(zip(*arr[::-1]))
    arr_2 = list(zip(*arr_1[::-1])) 
    arr_3 = list(zip(*arr_2[::-1]))

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(arr_1[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_2[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_3[i][j], end='')
        print()