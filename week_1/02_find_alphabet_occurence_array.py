# 최빈값 찾기_알파벳 빈도수 세기 (내가 짠 코드)
input = "hello my name is sparta"


def find_alphabet_occurrence_array(string):
    # 0으로 초기화 된 길이 26 배열 생성
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
