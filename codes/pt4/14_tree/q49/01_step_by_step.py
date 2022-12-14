import collections

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(
    n: int,
    edges: List[List[int]],
) -> List[int]:
    # 예외처리 하세요~
    if n <= 1:
        return [0]

    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫번째 리프노드 추가
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)

    # 루트 노드만 남을 때 까지 반복 제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves


test1 = [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]   # noqa

print(solution(n=10, edges=test1))
