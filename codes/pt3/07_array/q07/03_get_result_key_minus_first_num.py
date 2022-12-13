
from typing import List


def sums(
        nums: List[int],
        target: int,
) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 26
    print(sums(nums, target))
