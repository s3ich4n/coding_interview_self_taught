from typing import List


def solution(
    n: int,
    k: int,
) -> List[List[int]]:
    results = []

    def dfs(
        elements,
        start: int,
        k: int
    ):
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


print(solution(n=4, k=2))
