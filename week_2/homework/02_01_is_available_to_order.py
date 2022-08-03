# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오. (강의 답안)
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 이 문제는 단순히 특정한 문자열이 배열에 존재하는지만 확인하면 됨
# 정렬을 할 필요없이, 집합 자료형을 사용

# 내부적으로 파이썬은 set에 대해서 in 연산은 O(1)의 시간복잡도로 처리
# 내부적으로 파이썬은 list에 대해서 in연산을 O(N)의 시간복잡도로 처리
def is_available_to_order(menus, orders):
    # 교집합을 찾음
    intersection = set(menus) & set(orders)
    if set(orders) == intersection & set(orders):
        return True

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
