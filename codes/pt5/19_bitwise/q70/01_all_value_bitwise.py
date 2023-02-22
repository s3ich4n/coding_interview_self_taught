from typing import List


def single_number(nums: List[int]) -> int:
    result = 0

    for num in nums:
        result ^= num

    return result


nums = [4, 1, 2, 1, 2]
print(single_number(nums))
