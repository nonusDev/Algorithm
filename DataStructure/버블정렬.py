# Bubble Sort : 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 정렬 방식
# 시간 복잡도 : O(n^2)

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    
    return x

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]