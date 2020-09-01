# Counting Sort : 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여 임의의 배열에 넣어 정렬하는 방식
# 시간 복잡도 : O(n)


def conting_sort(x):
    for i in range(len(arr)):
        count[arr[i]] += 1
    
    # 카운트 배열을 순회하면서 앞 쪽의 값을 더함
    for j in range(1, len(count)):
        count[j] += count[j - 1]

    # 원본 배열의 뒤쪽부터 순회하면서 카운트 배열을 참조하여 정렬될 위치를 결정
    for k in range(len(arr)-1, -1, -1):
        tmp = arr[k]                    # 정렬하고자 하는 수
        idx = count[tmp] - 1
        res[idx] = tmp
        count[tmp] -= 1
    
    return res

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
count = [0] * 10                        # 카운트 배열 : 원본 배열의 가장 큰 값 + 1만큼의 크기 배열
res = [0] * len(arr)                    # 정렬 대상 배열