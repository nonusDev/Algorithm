import sys

sys.stdin = open("2007.패턴마디의길이.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(input())

    sol = {}
    cnt = 0
    for i in arr:
        sol[i] = arr.count(i)

    for i in sol.values():
        cnt += i // min(sol.values())

    print(f"#{tc} {cnt}")