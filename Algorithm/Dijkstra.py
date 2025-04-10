#coding=utf-8

import sympy as sym
# 输入一个整数，将值保存在变量 start
start = int(input())
# 用data数据构建邻接表，输出该邻接表。
# ***** Begin *****#

# ***** End *****#

data = [
    [0,1, 8], 
    [0,2, 1], 
    [0,6, 2], 
    [0,5, 4],
    [1,0, 8], 
    [1,2, 5], 
    [1,3, 10], 
    [1,6, 9],
    [2,1, 5], 
    [2,0, 1], 
    [3,1, 10],
    [3,6, 5], 
    [3,4, 8], 
    [3,5, 8], 
    [4,3, 8], 
    [4,5, 5], 
    [5,0, 4], 
    [5,6, 7],
    [5,3, 8], 
    [5,4, 5], 
    [6,1, 9], 
    [6,0, 2], 
    [6,3, 5], 
    [6,5, 7]
]

# 初始化各项数据
graph = [[] for _ in range(7)]
n = len(graph)
for edge in data:
    graph[edge[0]].append([edge[1], edge[2]])
# 把源点花费初始化为0，其他为无穷大（用99999代替）。
costs = [99999 for _ in range(n)]
costs[start] = 0

# 把各个顶点的父结点设置成-1。
parents = [-1 for _ in range(n)]

# 标记已确定好最短花销的点。
visited = [False for _ in range(n)]

# 已经确定好最短花销的点列表。
t = []

while len(t) < n:
    minCost = 99999
    minNode = None
    # 从costs里面找最小花销minCost和最小花销节点minNode。
    for i in range(n):
        if not visited[i] and costs[i] < minCost:
            minCost = costs[i]
            minNode = i
    # 将花销最小节点minNode添加到列表t 中，在vivisited中将该点的标记置为True。
    # ***** Begin *****#
    t.append(minNode)
    visited[minNode] = True
    # ***** End *****#
    # 从当前这个顶点出发，遍历与它相邻的顶点的边，计算最短通路，更新costs和parents
    for edge in graph[minNode]:
        if not visited[edge[0]] and minCost + edge[1] < costs[edge[0]]:
            costs[edge[0]] = minCost + edge[1]
            parents[edge[0]] = minNode
# 输出花费和前一节点的两个列表。
# ***** Begin *****#
print(graph)
print(costs)
print(parents)
# ***** End *****#