from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(
    preorder: List[int],
    inorder: List[int],
) -> TreeNode:
    if inorder:
        # 전위 순회결과는 중위 순회의 분할 인덱스
        index = inorder.index(preorder.pop(0))

        node = TreeNode(inorder[index])
        node.left = solution(preorder, inorder[0:index])
        node.right = solution(preorder, inorder[index + 1:])

        return node


# t1_preorder = [3, 9, 20, 15, 7]
# t1_inorder = [9, 3, 15, 20, 7]

# a = solution(
#     preorder=t1_preorder,
#     inorder=t1_inorder,
# )
# print(a)

t2_preorder = [1, 2, 4, 5, 3, 6, 7, 9, 8]
t2_inorder = [4, 2, 5, 1, 7, 9, 6, 8, 3]

b = solution(
    preorder=t2_preorder,
    inorder=t2_inorder,
)
print(b)
