class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(
        head: ListNode
) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next

        # THIS WILL NOT WORK AS YOU THINK
        rev, rev.next = slow, rev
        slow = slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


test4 = ListNode(val="1")
test3 = ListNode(val="2", next=test4)
test2 = ListNode(val="2", next=test3)
test1 = ListNode(val="1", next=test2)

is_palindrome(test1)
