import collections

from typing import List


def solution(
    num_courses: int,
    prerequisites: List[List[int]],
):
    """
    """

    graph = collections.defaultdict(list)

    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환구조면 False
        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False

        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색을 마친 값에 대한 노드 추가
        visited.add(i)

        return True

    # 순환구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True


test1 = (2, [[1, 0]])
test2 = (2, [[1, 0], [0, 1]])
test3 = (3, [[0, 1], [0, 2], [1, 2]])

# print(solution(*test1))
# print(solution(*test2))
print(solution(*test3))
