# array 를 따라가면서 target 이 존재한다면 True 를 반환하고,
# 끝까지 없다면 False 를 반환하는 간단한 코드를 이진 탐색의 방법으로 구현 (강의 답안)
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# // -> 나누기 결과값에서 소수점 버림
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
