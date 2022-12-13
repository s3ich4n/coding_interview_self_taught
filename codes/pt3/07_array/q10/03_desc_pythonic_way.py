from typing import *


def array_pair_sum(
        nums: List[int]
) -> int:
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    ar = [1, 4, 3, 2]
    print(array_pair_sum(ar))
