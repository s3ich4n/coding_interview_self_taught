import collections


from typing import List


def solution(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    # 그래프 순서대로 구성
    # tickets 값에 대해 정렬을 미리 해서 넣는다.
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(starting_point: str):
        # 첫번째 값을 읽고, 어휘 순으로 방문한다.
        while graph[starting_point]:
            dfs(graph[starting_point].pop(0))

        route.append(starting_point)

    dfs(starting_point='JFK')
    # 뒤집어서 어휘 순으로 리턴
    return route[::-1]


test1 = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"],
]

test2 = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]

# print(solution(test1))
print(solution(test2))
