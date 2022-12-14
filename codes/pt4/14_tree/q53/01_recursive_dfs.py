import sys

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def solution(self, root: TreeNode) -> int:
        if root.left:
            self.solution(root.left)

        # 중위순회를 하며 방금 찍었던 최소값과 지금 내 값이 같은지 기록
        # 현재값은 prev에 저장
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.solution(root.right)

        return self.result


# lv4
lv4_l1 = TreeNode(val=1, left=None, right=None)
lv4_l2 = TreeNode(val=3, left=None, right=None)
lv4_l3 = TreeNode(val=5, left=None, right=None)
lv4_l4 = TreeNode(val=7, left=None, right=None)
# lv3
lv3_l1 = TreeNode(val=2, left=lv4_l1, right=lv4_l2)
lv3_l2 = TreeNode(val=6, left=lv4_l3, right=lv4_l4)
# lv2
lv2_l = TreeNode(val=4, left=lv3_l1, right=lv3_l2)
lv2_r = TreeNode(val=12, left=None, right=None)
# lv1
lv1 = TreeNode(val=8, left=lv2_l, right=lv2_r)


s = Solution()
a = s.solution(lv1)
print(a)
