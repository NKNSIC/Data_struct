class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 顶点的数量
        self.graph = []  # 图的表示（边列表）

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def bellman_ford(self, src):
        # 初始化距离值
        distance = [float("Inf")] * self.V
        distance[src] = 0

        # 松弛所有边 |V| - 1 次
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # 检测负权循环
        for u, v, w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                return

        return distance

# 示例
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

src = 0
distance = g.bellman_ford(src)

if distance:
    print("Distance from vertex", src)
    for i in range(g.V):
        print(f"to vertex {i} is {distance[i]}")