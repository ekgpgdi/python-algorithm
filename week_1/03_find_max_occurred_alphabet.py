# 최빈값 찾기 (내가 짠 코드)
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    # 알파벳 빈도수 측정
    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord("a")
        alphabet_occurrence_array[index] += 1

    max_num = 0
    index = 0

    # 알파벳 빈도수 중 가장 큰 값을 찾음
    for idx in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[idx] > max_num:
            max_num = alphabet_occurrence_array[idx]
            index = idx

    # 알파벳 빈도수 중 가장 큰 값을 문자로 변환 -> chr() method convert number to char python
    return chr(index + ord("a"))


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))