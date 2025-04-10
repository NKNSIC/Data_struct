#include <stdio.h>

#define NODES 4 // 定义节点数量

// 打印闭包矩阵
void printClosure(int closure[NODES][NODES]) {
    printf("传递闭包矩阵:\n");
    for (int i = 0; i < NODES; i++) {
        for (int j = 0; j < NODES; j++) {
            printf("%d ", closure[i][j]);
        }
        printf("\n");
    }
}

// Warshall算法实现
void warshall(int graph[NODES][NODES]) {
    int closure[NODES][NODES];

    // 初始化闭包矩阵
    for (int i = 0; i < NODES; i++) {
        for (int j = 0; j < NODES; j++) {
            closure[i][j] = graph[i][j];
        }
    }

    // 计算传递闭包
    for (int k = 0; k < NODES; k++) {
        for (int i = 0; i < NODES; i++) {
            for (int j = 0; j < NODES; j++) {
                closure[i][j] = closure[i][j] || (closure[i][k] && closure[k][j]);
            }
        }
    }

    // 打印闭包矩阵
    printClosure(closure);
}

int main() {
    // 定义图的邻接矩阵
    int graph[NODES][NODES] = {
        {1, 1, 0, 0},
        {0, 1, 1, 0},
        {0, 0, 1, 1},
        {0, 0, 0, 1}
    };

    // 计算传递闭包
    warshall(graph);

    return 0;
}
