# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 한 바퀴 돌면서 길이를 알아낸 다음, 그 길이에서 k 만큼을 뺀 순서의 노드를 반환
    def get_kth_node_from_last(self, k):
        current_cur = self.head
        k_next_cur = current_cur

        for i in range(k):
            k_next_cur = k_next_cur.next

        while current_cur is not None:
            if k_next_cur is None:
                return current_cur
            k_next_cur = k_next_cur.next
            current_cur = current_cur.next


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
