# 배열에서 특정 요소 찾기
# 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환
input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:      # array의 길이만큼 아래 연산이 실행
        if element == number:  # 비교 연산 1번 실행
            return True
    return False
# 총 시간 복잡도는 N * 1 = N

result = is_number_exist(3, input)
print(result)

