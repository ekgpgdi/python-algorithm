# 삽입 정렬
input = [4, 6, 2, 9, 1]


# 시간 복잡도 : O(N^2)
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            # 이미 앞쪽이 정렬되어 있기에 더 비교할 필요가 없음
            else:
                break
    return array


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
