# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오
input = 20


def find_prime_list_under_number(number):
    array = []
    i = 2
    while i < number:
        j = 2
        while j < i:
            if i % j == 0:
                break
            j += 1
        else:
            array.append(i)
        i += 1

    return array


result = find_prime_list_under_number(input)
print(result)
