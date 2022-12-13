
from typing import List


def sums(
        nums: List[int],
        target: int,
) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 26
    print(sums(nums, target))
