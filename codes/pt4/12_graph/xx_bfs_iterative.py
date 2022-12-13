def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]

    while queue:
        # 값 넣은거의 맨 앞값을 빼면 큐와 진배없으므로...
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

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

# 루트값을 넣고 BFS 수행
print(iterative_bfs(1))
