# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오 (개선하기)

# 소수의 특징을 고려
# 주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
input = 20


def find_prime_list_under_number(number):
    array = []
    for num in range(2, number):
        for arr in array:
            if arr*arr > num * num:
                break
            if num % arr == 0:
                break
        else:
            array.append(num)

    return array


result = find_prime_list_under_number(input)
print(result)

# [개선 1] 2와 3으로 나누어 떨어지지 않는다면, 2 X 3 인 6으로도 당연히 안 나누어 떨어집니다.
# 즉, 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라,
# 2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보도록 개선 -> 직전에 찾은 소수를 이용

# [개선 2] 주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문입니다.
# 이를 이용해서 i * i ≤ n 일 때까지만 비교