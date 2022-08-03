# Q. 60에서 0까지 숫자를 출력하시오.
def count_down(number):
    if number < 0:         # 만약 숫자가 0보다 작다면, 탈출
        return

    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출


count_down(60)