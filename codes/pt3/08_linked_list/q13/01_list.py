from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 203쪽


def is_palindrome(
        head: ListNode
) -> bool:
    q: List = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    # while len(q) > 1:
    #     if q.pop(0) != q.pop():
    #         return False

    # return True

    return q == q[::-1]


# case 1)
test2 = ListNode(val="2")
test1 = ListNode(val="1", next=test2)

# case 2)
# test4 = ListNode(val="1")
# test3 = ListNode(val="2", next=test4)
# test2 = ListNode(val="2", next=test3)
# test1 = ListNode(val="1", next=test2)

print(is_palindrome(test1))
