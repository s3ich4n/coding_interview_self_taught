class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solution(
        self,
        t1: TreeNode,
        t2: TreeNode,
    ) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.solution(t1.left, t2.left)
            node.right = self.solution(t1.right, t2.right)
            return node

        else:
            # None 인 값 아니면 존재하는 값을 리턴.
            # 이렇게도 쓸 수 있구나...
            return t1 or t2


# lv3
t1_lv3_l1 = TreeNode(val=5, left=None, right=None)
# lv2
t1_lv2_l = TreeNode(val=3, left=t1_lv3_l1, right=None)
t1_lv2_r = TreeNode(val=2, left=None, right=None)
# lv1
t1_lv1 = TreeNode(val=1, left=t1_lv2_l, right=t1_lv2_r)

# lv3
t2_lv3_l2 = TreeNode(val=4, left=None, right=None)
t2_lv3_r2 = TreeNode(val=7, left=None, right=None)
# lv2
t2_lv2_l = TreeNode(val=1, left=None, right=t2_lv3_l2)
t2_lv2_r = TreeNode(val=3, left=None, right=t2_lv3_r2)
# lv1
t2_lv1 = TreeNode(val=2, left=t2_lv2_l, right=t2_lv2_r)

s = Solution()

a = s.solution(t1_lv1, t2_lv1)
print(a)
