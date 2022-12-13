from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(
        head: ListNode,
) -> ListNode:
    p = head
    lst: List = []

    while p:
        lst.append(p.val)
        p = p.next

    lst.sort()

    p = head
    for i in lst:
        p.val = i
        p = p.next

    return head


test5 = ListNode(val=4)
test4 = ListNode(val=3, next=test5)
test3 = ListNode(val=0, next=test4)
test2 = ListNode(val=5, next=test3)
test1 = ListNode(val=-1, next=test2)

sort_list(test1)
print(test1)
