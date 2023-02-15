import bisect

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        expected = target - v

        # 슬라이싱!
        i = bisect.bisect_left(numbers[k + 1:], expected)

        if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
            return k + 1, i + k + 2


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
