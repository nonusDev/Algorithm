for t in range(1, int(input())+1):
    number = list(map(int, input().split()))
    cnt = 0
 
    for i in number:
        if i % 2 == 1:
            cnt += i
     
    print(f"#{t} {cnt}")