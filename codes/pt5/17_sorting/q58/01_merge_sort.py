class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
        l1: ListNode,
        l2: ListNode,
) -> ListNode:
    # 둘 다 있어야 뭘 하겠죠?
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_two_lists(l1.next, l2)

    return l1 or l2


def sort_list(
        head: ListNode,
) -> ListNode:
    # 빈 리스트거나 하나짜리 리스트에 대한 예외처리
    if not (head and head.next):
        return head

    # runner 기법
    half, slow, fast = None, head, head

    while fast and fast.next:
        half, slow, fast = slow, slow.next, slow.next.next
    half.next = None

    # 분할재귀
    # l1, l2로 각각 분할한 리스트의 좌/우를 찾는다.
    l1 = sort_list(head)
    l2 = sort_list(slow)

    return merge_two_lists(l1, l2)


test5 = ListNode(val="4")
test4 = ListNode(val="3", next=test5)
test3 = ListNode(val="0", next=test4)
test2 = ListNode(val="5", next=test3)
test1 = ListNode(val="-1", next=test2)

sort_list(test1)
print(test1)
