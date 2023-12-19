from collections import defaultdict


def has_eulerian_circuit(graph):
    # 统计每个节点的出度和入度
    degrees = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            degrees[u] += 1
            degrees[v] -= 1

    # 检查每个节点的出度和入度是否相等
    for degree in degrees.values():
        if degree != 0:
            return False

    # 检查图是否连通
    visited = set()
    stack = [next(iter(graph))]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited) == len(graph)


# 测试示例
graph1 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
print(has_eulerian_circuit(graph1))  # 输出: True

graph2 = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1]
}
print(has_eulerian_circuit(graph2))  # 输出: True