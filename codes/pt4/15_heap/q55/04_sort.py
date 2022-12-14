from typing import List


def solution(
    nums: List[int],
    k: int
) -> int:
    nums.sort()
    return nums[-k]


print(solution([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
