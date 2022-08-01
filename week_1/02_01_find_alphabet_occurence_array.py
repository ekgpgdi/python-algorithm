# 최빈값 찾기_알파벳 빈도수 세기
input = "hello my name is sparta"


def find_alphabet_occurrence_array(string):
    # 0으로 초기화 된 길이 26 배열 생성
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        # 들어온 문자가 알파벳인지 확인
        if alphabet.isalpha():
            # 알파벳을 숫자로 변환 -> ord() method to convert each letter to a number.
            index = ord(alphabet) - ord('a')
            alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
