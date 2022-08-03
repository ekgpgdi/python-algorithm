# 선택 정렬
input = [4, 6, 2, 9, 1]


# 시간 복잡도 = O(N^2)
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        print(array)
        min_index = i
        for j in range(i, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
