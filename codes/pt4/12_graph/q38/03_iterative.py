import collections


from typing import List


def solution(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    # 그래프 순서대로 구성
    # tickets 값에 대해 정렬을 미리 해서 넣는다.
    for a, b in sorted(tickets):
        graph[a].append(b)

    # 변수를 받거나 해서...
    # 특정 값부터 시작할 수 있도록 처리가 필요할지도?
    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성.
        # 하지만, 막히는 부분에서는 처리가 필요
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

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

# 경로가 끊어지는 경우
test3 = [
    ["JFK", "KUL"],
    ["JFK", "NRT"],
    ["NRT", "JFK"],
]

# print(solution(test1))
# print(solution(test2))
print(solution(test3))
