from typing import List

from codec import Codec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    val: int = 0

    def solution(self, root: TreeNode) -> TreeNode:
        # 중위순회 하면서 기존에 지나왔던 합계를 더해준다.
        if root:
            self.solution(root.right)
            self.val += root.val
            root.val = self.val
            self.solution(root.left)

        return root


# lv4
lv4_l4 = TreeNode(val=3, left=None, right=None)
lv4_r4 = TreeNode(val=8, left=None, right=None)
# lv3
lv3_l1 = TreeNode(val=0, left=None, right=None)
lv3_l2 = TreeNode(val=2, left=None, right=lv4_l4)
lv3_r1 = TreeNode(val=5, left=None, right=None)
lv3_r2 = TreeNode(val=7, left=None, right=lv4_r4)
# lv2
lv2_l = TreeNode(val=1, left=lv3_l1, right=lv3_l2)
lv2_r = TreeNode(val=6, left=lv3_r1, right=lv3_r2)
# lv1
lv1 = TreeNode(val=4, left=lv2_l, right=lv2_r)


s = Solution()
a = s.solution(lv1)
c = Codec()
print(c.serialize(a))
