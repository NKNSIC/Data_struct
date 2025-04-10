def floyd_warshall(graph):
    # 初始化距离矩阵
    dist = [[float('inf')] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        dist[i][i] = 0

    # 填充直接边的权重
    for u, neighbors in enumerate(graph):
        for v, weight in neighbors.items():
            dist[u][v] = weight

    # 动态规划更新距离矩阵
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # 如果通过顶点k的路径更短，则更新距离
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# 示例图
graph = {
    0: {1: 3, 3: 8},
    1: {0: 3, 2: 1, 3: 2},
    2: {1: 1, 3: 7},
    3: {0: 8, 1: 2, 2: 7}
}

# 计算所有顶点对之间的最短路径
shortest_paths = floyd_warshall(graph)

# 打印结果
for i, paths in enumerate(shortest_paths):
    print(f"Shortest paths from vertex {i}:")
    for j, path in enumerate(paths):
        print(f"to vertex {j}: {path}")