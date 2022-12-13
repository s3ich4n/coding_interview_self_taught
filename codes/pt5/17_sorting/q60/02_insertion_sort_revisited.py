class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertion_sort_list(
        head: ListNode,
) -> ListNode:
    # None 부터 시작
    cur = parent = ListNode(0)

    # 끝까지 순회
    while head:
        # cur.next가 있고
        # 현재값보다 cur.next의 값이 더 크면
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        # cur에는 head.next와 cur.next 로...
        # 맨 왼쪽부터 언패킹되면서 하나씩 실행된다. 동시에 되는건 없음.
        # xx_unpacking_dis.py 실행결과를 살펴보삼
        # 다만, 참조할 때의 차이가 있어서 이렇게 한거임
        # 몇번의 트랜잭션만에 되는지가 중요한데, 파이썬은 이렇게 해야 한번에 돼요
        cur.next, head.next, head = head, cur.next, head.next

        # 얘는 다시 "처음으로" 되돌아가서
        # 삽입정렬 할 수 있도록 세팅한다.
        #
        # 다음 head가 cur보다 큰 상태면 굳이 돌아갈 필요가 없다.
        #
        if head and cur.val > head.val:
            cur = parent

    # None 다음부터인 ListNode는 정렬되어있다.
    return parent.next


test4 = ListNode(val=3)
test3 = ListNode(val=1, next=test4)
test2 = ListNode(val=-2, next=test3)
test1 = ListNode(val=4, next=test2)

output = insertion_sort_list(test1)
print(output)
