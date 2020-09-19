for t in range(1, int(input())+1):
    number = list(map(int, input().split()))
    cnt = 0

    for i in number:
        cnt += i
        result = round(cnt / 10)
    
    print(f"#{t} {result}")