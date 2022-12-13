from typing import List


def iterative_dfs(
    start_vertex,
):
    discovered = []
    stack = [start_vertex]

    # 스택이 빌 때 까지...
    while stack:
        vertex = stack.pop()
        # 스택서 pop한 순서이기 때문에
        # 역순방문을 진행한다!
        if vertex not in discovered:
            discovered.append(vertex)
            for w in graph[vertex]:
                stack.append(w)

    return discovered


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# 루트값을 넣고 DFS 수행
print(iterative_dfs(1))
