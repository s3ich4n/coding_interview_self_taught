class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter: int = 0

    def solution(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            # 왼쪽, 오른쪽의 각 리프노드 검색
            left = dfs(node.left)
            right = dfs(node.right)

            # diameter
            self.diameter = max(self.diameter, 2 + left + right)
            # 높이
            return max(left, right) + 1

        dfs(root)
        return self.diameter


lv3_l1 = TreeNode(val=4, left=None, right=None)
lv3_l2 = TreeNode(val=5, left=None, right=None)
lv2_r = TreeNode(val=3, left=None, right=None)
lv2_l = TreeNode(val=2, left=lv3_l1, right=lv3_l2)
lv1 = TreeNode(val=1, left=lv2_l, right=lv2_r)

s = Solution()

print(s.solution(lv1))
