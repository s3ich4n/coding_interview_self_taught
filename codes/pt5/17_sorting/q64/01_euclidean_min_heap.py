import math
import heapq

from typing import List


def k_closest(
    points: List[List[int]],
    k: int,
) -> List[List[int]]:
    heap = []

    for (x, y) in points:
        # 본디 일케 푸는게 맞으나
        # dist = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
        #
        # 이런식으로 깔끔하게 처리할 수도 있겠지
        dist = x ** 2 + y ** 2
        heapq.heappush(heap, (dist, x, y))

    result = []
    for _ in range(k):
        (dist, x, y) = heapq.heappop(heap)
        result.append([x, y])
    
    return result


points1 = [[1, 3], [-2, 2]]
k1 = 1

print(k_closest(points1, k1))

points2 = [[3, 3], [5, -1], [-2, 4]]
k2 = 2

print(k_closest(points2, k2))
