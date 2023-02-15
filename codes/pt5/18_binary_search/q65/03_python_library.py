import bisect

from typing import List


def search(nums: List[int], target: int) -> int:
    # nums 배열서 target 을 찾으라
    # 몇번 째 index겠느냐
    index = bisect.bisect_left(nums, target)

    # index가 유효 범위 내에있고, index번째 값이 찾는 값이면?
    if index < len(nums) and nums[index] == target:
        return index
    
    else:
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(search(nums, target))
