from typing import List


def solution(
        candidates: List[int],
        target: int
) -> List[List[int]]:
    result = []

    def dfs(
        csum,
        index,
        path,
    ):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위원소 까지의 나열 재귀 호출
        # 여기가 사실상 핵심!
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


print(solution([2, 3, 6, 7], target=7))
# print(solution([2, 3, 5], target=8))
