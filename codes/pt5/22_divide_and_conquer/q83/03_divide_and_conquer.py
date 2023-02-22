from typing import List


def majority(nums: List[int]) -> int:

    if not nums:
        return None

    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = majority(nums[:half])
    b = majority(nums[half:])

    # 0번째나 1번째냐를 판가름하는 로직.
    return [b, a][nums.count(a) > half]


q1 = [2, 2, 1, 1, 1, 2, 2]
print(majority(nums=q1))
