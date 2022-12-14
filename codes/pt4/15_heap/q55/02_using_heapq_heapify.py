import heapq

from typing import List


def solution(
    nums: List[int],
    k: int
) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums), k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


print(solution([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
