import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(
    root: TreeNode,
):
    if root is None:
        return 0
    queue = collections.deque([root])

    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            # 왼쪽루트 꺼내오고
            cur_root = queue.popleft()

            # 순회하기 위한 append, 즉 BFS다
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    return depth


lv3_r1 = TreeNode(val=15, left=None, right=None)
lv3_r2 = TreeNode(val=7, left=None, right=None)
lv2_r = TreeNode(val=20, left=lv3_r1, right=lv3_r2)
lv2_l = TreeNode(val=9, left=None, right=None)
lv1 = TreeNode(val=3, left=lv2_l, right=lv2_r)


print(solution(lv1))
