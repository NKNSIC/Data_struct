def warshall_algorithm(graph):
    n = len(graph)
    closure = [[0 if i != j and graph[i][j] == 0 else 1 for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure

# 示例图
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

# 计算传递闭包
closure = warshall_algorithm(graph)

# 输出结果
for row in closure:
    print(row)