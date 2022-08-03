# Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.
input = "abcba"


# 반복문을 사용하여 해결
# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n - 1 - i]:
#             return False
#     return True

# 재귀함수를 이용하여 해결
def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


print(is_palindrome(input))
