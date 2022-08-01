# Q. 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    check0 = 0
    check1 = 0
    
    for idx in range(len(string)):
        if idx == 0:
            if string[idx] == "0":
                check0 += 1
            else:
                check1 += 1
        else:
            if string[idx - 1] != string[idx]:
                if string[idx] == "0":
                    check0 += 1
                else:
                    check1 += 1

    return min(check0, check1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)