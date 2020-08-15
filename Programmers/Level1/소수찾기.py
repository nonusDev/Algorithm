def solution(n):
    sol = [0, 0]+[1] * (n-1)
    cnt = 0
    for i in range(2, n+1):
        if sol[i]:
            cnt += 1
        for j in range(2*i, n+1, i):
            sol[j] = 0
    
    return cnt
    
# 1
n = 10

# 2
n = 5