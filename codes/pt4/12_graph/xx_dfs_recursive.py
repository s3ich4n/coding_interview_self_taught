from typing import List


def recursive_dfs(
    v,
    discovered: List = []
):
    discovered.append(v)

    # 쫓아가보면 금방 이해함
    for index in graph[v]:
        if index not in discovered:
            discovered = recursive_dfs(index, discovered)

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
print(recursive_dfs(1))
