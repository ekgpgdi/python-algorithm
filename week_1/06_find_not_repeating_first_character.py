# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오. (내가 짠 코드)
input = "abadabac"


def find_not_repeating_character(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if i == j:
                continue
            if string[i] == string[j]:
                break
        else:
            return string[i]

    return "_"


result = find_not_repeating_character(input)
print(result)
