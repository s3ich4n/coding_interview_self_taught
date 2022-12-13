# 213쪽

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
        l1: ListNode,
        l2: ListNode,
) -> ListNode:
    if (not l1) or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1

    # 백트래킹을 하면서 마지막에 더이상 정렬 할 필요가 없으면
    # 정렬 완료한 맨 뒤에서부터 앞으로(백트래킹하며) 나온다.
    if l1:
        # 재귀하면서 l1에 정렬된 값을 계속해서 모은다.
        l1.next = merge_two_lists(l1.next, l2)

    return l1


input1_3 = ListNode(val=4)
input1_2 = ListNode(val=2, next=input1_3)
input1_1 = ListNode(val=1, next=input1_2)

input2_3 = ListNode(val=4)
input2_2 = ListNode(val=3, next=input2_3)
input2_1 = ListNode(val=1, next=input2_2)

print(merge_two_lists(input1_1, input2_1))
