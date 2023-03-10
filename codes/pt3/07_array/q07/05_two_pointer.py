from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    """
    투포인터는 정렬된 형식으로 가야한다!!!!
    """
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
