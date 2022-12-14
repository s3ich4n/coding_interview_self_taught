from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(
    root: TreeNode,
    L: int,
    R: int,
) -> int:
    if not root:
        return 0

    # DFS로 "전체"를 브루트포스한다!
    is_value_in_them = (root.val if L <= root.val <= R else 0)
    left_value = solution(root.left, L, R)
    right_value = solution(root.right, L, R)

    return is_value_in_them + left_value + right_value


# lv4
# lv4_l4 = TreeNode(val=3, left=None, right=None)
# lv4_r4 = TreeNode(val=8, left=None, right=None)
# lv3
lv3_l1 = TreeNode(val=3, left=None, right=None)
lv3_l2 = TreeNode(val=7, left=None, right=None)
# lv3_r1 = TreeNode(val=5, left=None, right=None)
lv3_r2 = TreeNode(val=18, left=None, right=None)
# lv2
lv2_l = TreeNode(val=5, left=lv3_l1, right=lv3_l2)
lv2_r = TreeNode(val=15, left=None, right=lv3_r2)
# lv1
lv1 = TreeNode(val=10, left=lv2_l, right=lv2_r)


a = solution(
    lv1,
    L=7,
    R=15,
)
print(a)
