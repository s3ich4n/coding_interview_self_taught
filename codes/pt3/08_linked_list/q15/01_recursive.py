class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 203쪽


def reverse_recursively(
        head: ListNode
) -> bool:
    def rev(
            node: ListNode,
            prev: ListNode = None,
    ):
        print(f"id(node): 0x{id(node):x}, id(prev): 0x{id(prev):x}")
        if not node:
            return prev
        # 여기서 스왑. 이게 핵심!
        next, node.next = node.next, prev
        print(f"id(next): 0x{id(next):x}, id(node): 0x{id(node):x}")
        return rev(next, node)

    return rev(head)


# case 1)
test5 = ListNode(val="5")
test4 = ListNode(val="4", next=test5)
test3 = ListNode(val="3", next=test4)
test2 = ListNode(val="2", next=test3)
test1 = ListNode(val="1", next=test2)

print(f"input id: 0x{id(test1):x}")
output = reverse_recursively(test1)
print(f"output id: 0x{id(output):x}")
