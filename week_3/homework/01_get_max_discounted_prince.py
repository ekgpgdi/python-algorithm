# Q. 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid_index = len(array) // 2
    left_array = array[:mid_index]
    right_index = array[mid_index:]
    return merge(merge_sort(left_array), merge_sort(right_index))


def merge(array1, array2):
    merge_array = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] > array2[array2_index]:
            merge_array.append(array1[array1_index])
            array1_index += 1
        else:
            merge_array.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            merge_array.append(array2[array2_index])
            array2_index += 1
    else:
        while array1_index < len(array1):
            merge_array.append(array1[array1_index])
            array1_index += 1

    return merge_array


def get_max_discounted_price(prices, coupons):
    sort_prices = merge_sort(prices)
    sort_coupons = merge_sort(coupons)

    total_price = 0

    for index in range(len(sort_coupons)):
        if index >= len(prices):
            return int(total_price)

        total_price += sort_prices[index] * ((100 - sort_coupons[index]) / 100)

    for index in range(len(sort_coupons), len(sort_prices)):
        total_price += sort_prices[index]

    return int(total_price)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
