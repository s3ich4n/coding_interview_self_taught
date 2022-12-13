import collections
import heapq

from typing import List


def solution(
    times: List[List[int]],
    N: int,
    K: int,
) -> int:
    graph = collections.defaultdict(list)

    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(시작지점, 도착지점, 가격)]
    # 최소값만 담기게 됨. 아래에서 heappop을 해주니까.
    k = 0
    Q = [(0, src, k)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지의 최단경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            #
            # prev[v] <- u 는 빠져있다. 이전 노드는 여기서는 중요하지 않아서.
            # 필요하면 추가하기.
            # 이전 노드를 쫓아가려면 어떻게 해야하는지 생각해보자. 걍 순서대로 넣으면 될 것 같다.
            #

            # 여기에서는 우선순위를 조절.
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    if len(dist) == N:
        return max(dist.values())

    return -1


test1 = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1],
]
print(solution(test1, N=4, K=2))


# test2 = [
#     [3, 1, 5],
#     [3, 2, 2],
#     [2, 1, 2],
#     [3, 4, 1],
#     [4, 5, 1],
#     [5, 6, 1],
#     [6, 7, 1],
#     [7, 8, 1],
#     [8, 1, 1],
# ]
# print(solution(test2, N=8, K=3))
