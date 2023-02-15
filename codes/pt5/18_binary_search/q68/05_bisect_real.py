import bisect

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        expected = target - v

        #
        # lo 키워드가 왼쪽 범위를 제한하는 값이다.
        # 기본값: lo=0, hi=len(a)
        # E.g., bisect.bisect_left(a, x, lo=0, hi=len(a))
        #
        i = bisect.bisect_left(numbers, expected, lo=k + 1)

        if i < len(numbers) and numbers[i] == expected:
            return k + 1, i + 1


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))