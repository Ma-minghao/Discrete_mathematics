import sys as s

s.setrecursionlimit(100000000)

# 弗洛伊德算法
# 1，从任意一条单边路径开始。所有两点之间的距离是边的权，如果两点之间没有边相连，则权为无穷大。
# 2，对于每一对顶点 u 和 v，看看是否存在一个顶点 w 使得从 u 到 w 再到 v 比已知的路径更短。如果是更新它。
# 把图用邻接矩阵G表示出来，如果从Vi到Vj有路可达，则G[i][j]=d，d表示该路的长度；否则G[i][j]=无穷大。
# 定义一个矩阵D用来记录所插入点的信息，D[i][j]表示从Vi到Vj需要经过的点，初始化D[i][j]=j。
# 把各个顶点插入图中，比较插点后的距离与原来的距离，G[i][j] = min( G[i][j], G[i][k]+G[k][j] )，如果G[i][j]的值变小，则D[i][j]=k。
# 在G中包含有两点之间最短道路的信息，而在D中则包含了最短通路径的信息。
# 比如，要寻找从V5到V1的路径。根据D，假如D(5,1)=3则说明从V5到V1经过V3，路径为{V5,V3,V1}，如果D(5,3)=3，说明V5与V3直接相连，如果D(3,1)=1，说明V3与V1直接相连。

def floyd():
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]  # 更新距离
                    parents[i][j] = parents[k][j]  # 更新父结点


# 打印路径
def print_path(i, j):
    if i != j:
        print_path(i, parents[i][j] - 1)
    print(j + 1, end='->')


datas = [
    [1, 2, 4], [1, 3, 8],
    [2, 1, 4], [2, 3, 11], [2, 4, 8],
    [3, 1, 8], [3, 5, 1],
    [4, 2, 8], [4, 5, 8], [4, 6, 7], [4, 7, 4],
    [5, 3, 1], [5, 4, 8], [5, 7, 2],
    [6, 4, 7], [6, 7, 14], [6, 8, 9],
    [7, 4, 4], [7, 5, 2], [7, 6, 14], [7, 8, 10],
    [8, 6, 9], [8, 7, 10]
]
n = 8
# 定义无穷大
inf = 9999999999
# 初始图的权值数据
graph = [[(lambda x: 0 if x[0] == x[1] else inf)([i, j]) for j in range(n)] for i in range(n)]
parents = [[i + 1] * n for i in range(n)]  # 关键地方，i-->j 的父结点初始化都为i
for u, v, c in datas:
    graph[u - 1][v - 1] = c  # 因为是有向图，边权只赋给graph[u][v]
    # graph[v][u] = c # 如果是无向图，要加上这条。

floyd()

print('Weight:')
for row in graph:
    for e in row:
        print('∞' if e == inf else e, end='\t')
    print()
print()
print('Path:')

for i in range(n):
    for j in range(n):
        print('Path({}->{}): '.format(i + 1, j + 1), end='')
        print_path(i, j)
        print(' Weight:', graph[i][j])