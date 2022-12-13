import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solution(self, root: TreeNode) -> int:
        queue = collections.deque([root])

        # 부모 노드부터 하향식으로 스왑을 수행
        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root


# lv3
lv3_r1 = TreeNode(val=6, left=None, right=None)
lv3_r2 = TreeNode(val=9, left=None, right=None)
lv3_l1 = TreeNode(val=1, left=None, right=None)
lv3_l2 = TreeNode(val=3, left=None, right=None)
# lv2
lv2_l = TreeNode(val=2, left=lv3_l1, right=lv3_l2)
lv2_r = TreeNode(val=7, left=lv3_r1, right=lv3_r2)
# lv1
lv1 = TreeNode(val=4, left=lv2_l, right=lv2_r)

s = Solution()

print(s.solution(lv1))
