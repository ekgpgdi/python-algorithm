# 최빈값 찾기
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]
    # 빈도수의 최댓값
    max_occurrence = 0
    # 가장 많이 있는 알파벳
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        # 문자열 내에 동일한 알파벳이 있는지 확인
        for char in string:
            if char == alphabet:
                occurrence += 1

        # 문자열 내에 동일한 알파벳의 빈도가 최댓값보다 큰지 비교
        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))