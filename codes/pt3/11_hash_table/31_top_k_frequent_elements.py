import heapq
import collections

from typing import *


def solution(
    nums: List[int],
    k: int,
) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []

    # 힙에 음수로 삽입
    # 키 밸류 뒤집어서 추가
    for index in freqs:
        heapq.heappush(freqs_heap, (-freqs[index], index))

    top_k = list()
    # k회만큼 추출. min heap 이므로 가장 작은 음수 순으로 추출함
    for _ in range(k):
        top_k.append(heapq.heappop(freqs_heap)[1])

    return top_k


test1 = [1, 1, 1, 2, 2, 3]
k = 2

print(solution(test1, k))
