class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 203쪽


def reverse_recursively(
        head: ListNode
) -> bool:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


# case 1)
test5 = ListNode(val="5")
test4 = ListNode(val="4", next=test5)
test3 = ListNode(val="3", next=test4)
test2 = ListNode(val="2", next=test3)
test1 = ListNode(val="1", next=test2)

print(f"input id: 0x{id(test1):x}")
output = reverse_recursively(test1)
print(f"output id: 0x{id(output):x}")
