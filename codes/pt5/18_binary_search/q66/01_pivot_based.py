from typing import List


def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    # 1. 최소값 찾기
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        
        else:
            right = mid

    pivot = left

    # 2. 피벗 기준 이진검색
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1

        elif nums[mid_pivot] > target:
            right = mid - 1

        else:
            return mid_pivot

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 1

print(search(nums, target))
