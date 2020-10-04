# 재귀함수를 이용하여 Factorial을 작성하시오.

def factorial(n):
    # 재귀를 작성할 때는, 더이상 재귀가 호출되지 않는 영역을 설정(기저영역)
    if n == 1:
        return 1
    return n * factorial(n-1)

result = factorial(5)
print(result)

# 반복문을 이용하여 Factorial을 작성하시오.

# N = 5
# result = 1
# for i in range(1, N+1):
#     result *=  i
# print(result)

# 1부터 n까지의 합을 구하는 재귀 함수를 작성하시오.

# def n_sum(n):
#     if n == 1:
#         return 1
#     return n + n_sum(n-1)

# print(n_sum(5))