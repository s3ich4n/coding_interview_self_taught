from typing import *


def array_pair_sum(
        nums: List[int]
) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


if __name__ == "__main__":
    ar = [1, 4, 3, 2]
    print(array_pair_sum(ar))
