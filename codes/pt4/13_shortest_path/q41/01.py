#
# 이 문제는 공부 전, 반드시 이 이슈를 볼 것!
#   기존 책의 풀이는 노드/엣지가 길어지면 타임아웃이 난다.
#   dst를 못만나고 k가 0보다 크기만 하면 방문하므로, 중복탐색을 한다
# https://github.com/onlybooks/algorithm-interview/issues/104
#

import collections
import heapq
import sys

from typing import List


def solution(
    n: int,
    flights: List[List[int]],
    src: int,
    dst: int,
    K: int,
) -> int:
    graph = collections.defaultdict(list)

    # 가중치가 추가됨!
    # (
    #   flights 의 n번 노드로 가기까지에 대한 현재 가중치,
    #   K값 (탐색 한번 할 때마다 -1이 계속되겠죠?)
    # )
    weight = [(sys.maxsize, K)] * n

    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                # 1. 가중치 값이 작거나
                # 2. 탐색하는 횟수가 최소 경유지 수보다 길다면?
                if alt < weight[v][0] or k-1 >= weight[v][1]:
                    weight[v] = (alt, k-1)
                    heapq.heappush(Q, (alt, v, k - 1))

    return -1


# print(solution(
#     n=3,
#     flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
#     src=0,
#     dst=2,
#     K=0,
# ))

# 예상해답 200
# print(solution(
#     n=4,
#     flights=[[0, 1, 100], [0, 2, 100], [0, 3, 200], [1, 3, 300], [2, 3, 400]],
#     src=0,
#     dst=3,
#     K=0,
# ))

# 예상해답 400
print(solution(
    n=5,
    flights=[[0, 1, 100], [0, 2, 100], [0, 3, 600], [1, 3, 300], [2, 3, 400]],
    src=0,
    dst=3,
    K=1,
))
