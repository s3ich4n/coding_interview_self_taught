from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(nums: List[int]) -> TreeNode:
    # 예외처리
    if not nums:
        return None

    mid = len(nums) // 2

    # 분할정복. 재귀해서 처리합시다
    node = TreeNode(nums[mid])
    node.left = solution(nums[:mid])
    node.right = solution(nums[mid + 1:])

    return node


test1 = [-10, -7, -3, 0, 5, 7, 9]

a = solution(test1)
print(a)
