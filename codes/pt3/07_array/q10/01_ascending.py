from typing import *


def array_pair_sum(
        nums: List[int]
) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


if __name__ == "__main__":
    ar = [1, 4, 3, 2]
    print(array_pair_sum(ar))
