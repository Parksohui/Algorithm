def bfs(graph, start, depth):
    queue = [start]

    while queue:
        temp = queue.pop(0)
        for i in graph[temp]:
            if depth[i] == 0 and i != 1:  # 아직 방문하지 않은 곳
                depth[i] = depth[temp] + 1  # depth
                queue.append(i)
    return depth


def solution(n, edge):
    answer = 0

    graph = {}
    depth = [0] * (n + 1)

    for i in range(n):
        graph[i + 1] = []

    for i in edge:  # graph
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    result = bfs(graph, 1, depth)

    find = max(result)  # 가장 멀리 떨어진 노드

    for value in result:
        if value == find:
            answer += 1

    return answer