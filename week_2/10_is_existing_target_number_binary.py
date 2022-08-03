# array 를 따라가면서 target 이 존재한다면 True 를 반환하고,
# 끝까지 없다면 False 를 반환하는 간단한 코드를 이진 탐색의 방법으로 구현
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    index = len(array) // 2
    pre_index = index

    while target != array[index]:
        if target > array[index]:
            pre_index = index
            index = index + (len(array) - index) // 2
        else:
            index = (index - pre_index) // 2 + pre_index

        if target > array[index] > target:
            return False

    return True


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
