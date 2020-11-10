import sys

sys.stdin = open("1216.회문2.txt", 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    arr1 = list(zip(*arr))

    res = 0
    c_tmp = 0
    r_tmp = 0
    for i in range(100):
        for j in range(1, 101):
            for k in range(100):
                if arr[i][k:k+j] == arr[i][k:k+j][::-1]:
                    c_tmp = len(arr[i][k:k+j])
                if arr1[i][k:k+j] == arr1[i][k:k+j][::-1]:
                    r_tmp = len(arr1[i][k:k+j])
                    if res < r_tmp:
                        res = r_tmp
                    if res < c_tmp:
                        res = c_tmp
    print(res)
