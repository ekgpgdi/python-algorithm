# 최댓값 찾기_방법 (내가 짠 코드)
input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for num in array:
        if max_num < num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)