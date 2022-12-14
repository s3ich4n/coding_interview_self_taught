import heapq

from typing import List


def solution(
    nums: List[int],
    k: int
) -> int:
    # k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴됨.
    return heapq.nlargest(k, nums)[-1]


print(solution([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
