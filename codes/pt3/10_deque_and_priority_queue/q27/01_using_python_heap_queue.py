import heapq

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 연결리스트의 루트를 힙에 저장
    # (min heap 이므로 알아서 우선순위에 맞게 저장됨)
    for i in range(len(lists)):
        if lists[i]:
            # 값, i번째 리스트, i번째 리스트 참조를 담아 저장
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        # 힙에 push 한걸 하나씩 빼면서 순서를 맞춰줌
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            # 순서가 맞는걸 heap 에 다시 넣고
            # 위에서 다시 빼서 순서를 맞춰주기를 바라면 됨.
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next


test3 = ListNode(val="5")
test2 = ListNode(val="4", next=test3)
test1 = ListNode(val="1", next=test2)

test13 = ListNode(val="4")
test12 = ListNode(val="3", next=test13)
test11 = ListNode(val="1", next=test12)

test22 = ListNode(val="6")
test21 = ListNode(val="2", next=test22)

question = [test1, test11, test21]
a = solution(question)
print(a)
