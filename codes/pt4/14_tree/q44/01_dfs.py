class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int = 0

    def solution(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            # 왼쪽, 오른쪽의 각 리프노드 검색 (DFS, 재귀)
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드와 자식노드가 동일하면 거리 +1 증가
            # 맨 아래서부터 타고 올라오니까
            # 백트래킹 되면서 가장 긴 녀석을 구한다고 할 수 있다.
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 백트래킹 되면서,
            # 좌/우에서 자식 노드 간 거리의 합 최댓값이 결과로 나온다.
            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


lv3_r2 = TreeNode(val=5, left=None, right=None)
lv3_l1 = TreeNode(val=1, left=None, right=None)
lv3_l2 = TreeNode(val=1, left=None, right=None)
lv2_r = TreeNode(val=5, left=None, right=lv3_r2)
lv2_l = TreeNode(val=4, left=lv3_l1, right=lv3_l2)
lv1 = TreeNode(val=5, left=lv2_l, right=lv2_r)

s = Solution()

print(s.solution(lv1))
