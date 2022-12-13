import heapq
import collections

from typing import *


def solution(
    nums: List[int],
    k: int,
) -> List[int]:
    # zip: 여러 시퀀스에서 동일한 인덱스의 아이템을 순서대로 추출한 후 튜플로 zip해줌.
    answer = list(zip(*collections.Counter(nums).most_common(k)))[0]

    return answer


test1 = [1, 1, 1, 2, 2, 3]
k = 2

print(solution(test1, k))
