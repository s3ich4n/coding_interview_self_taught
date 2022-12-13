import itertools

from typing import List


def solution(
    n: int,
    k: int,
) -> List[List[int]]:
    # E.g., combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
    return list(itertools.combinations(range(1, n + 1), k))


print(solution(n=4, k=2))
