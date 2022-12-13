class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 203쪽


def is_palindrome(
        head: ListNode
) -> bool:
    rev = None
    slow = fast = head

    # Runner를 이용한 역순 연결리스트 구성
    while fast and fast.next:
        fast = fast.next.next

        # 이유가있는 코드임!
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    # 역순 리스트를 다 만들었으면 팰린드롬인지 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


# case 1)
# test2 = ListNode(val="2")
# test1 = ListNode(val="1", next=test2)

# case 2)
# test4 = ListNode(val="1")
# test3 = ListNode(val="2", next=test4)
# test2 = ListNode(val="2", next=test3)
# test1 = ListNode(val="1", next=test2)

# case 3)
test6 = ListNode(val="1")
test5 = ListNode(val="2", next=test6)
test4 = ListNode(val="4", next=test5)
test3 = ListNode(val="3", next=test4)
test2 = ListNode(val="2", next=test3)
test1 = ListNode(val="1", next=test2)

"""
case 3 해설)
1->2->3->4->2->1 의 경우...

1st:
fast: 3->4
rev: 1->2
rev.next: None
slow: 2->3
slow.next: 3->4

2nd:
fast: 2->1
rev: 2->3
rev.next: 1->None
slow: 3->4
slow.next: 4->2

3rd:
fast: None
rev: 3->4
rev.next: 2->1
slow: 4->2
slow.next: 2->1

---
fast가 None이므로, slow.next를 가서 보정해줄 필요가 없음.

---
rev.val과 slow.val이 같은지 일일이 보면 됨.
rev는 3->2->1을 볼거고
slow는 4->2->1을 볼테니

3->2->1
4->2->1

서로 비교해보면 됨... False니까 무한루프 나오고
rev가 값이 있으니, 여기에 not을 붙이면 False 리턴.
"""

print(is_palindrome(test1))
