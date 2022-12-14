import heapq

from typing import List


def solution(
    nums: List[int],
    k: int
) -> int:
    heap = list()
    for n in nums:
        # 음수로 저장해서 가장 낮은 수부터 추출 후 부호를 변환
        # 최대 힙처럼 동작함
        heapq.heappush(heap, -n)

    for _ in range(1, k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


print(solution([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
