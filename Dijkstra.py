G = {
    1: {1: 0, 2: 4, 3: 8},
    2: {1: 4, 2: 0, 3: 11, 4: 8},
    3: {1: 8, 3: 0, 5: 1},
    4: {2: 8, 4: 0, 5: 8, 6: 7, 7: 4},
    5: {3: 1, 4: 8, 5: 0, 7: 2},
    6: {4: 7, 6: 0, 7: 14, 8: 9},
    7: {4: 4, 5: 2, 6: 14, 7: 0, 8: 10},
    8: {6: 9, 7: 10, 8: 0}
}


# 1.初始化：给定一个起始顶点，将该顶点到其他顶点的最短路径初始化为无穷大。
# 2.选择当前最短路径长度最小的顶点A，将A标记为已访问。
# 3.更新最短路径：遍历A的邻接顶点B，如果经过A到达B的路径长度小于当前B的最短路径长度，则更新最短路径长度。
# 4.选择下一个最短路径长度最小的未访问顶点，重复步骤3。
# 5.重复步骤4，直到所有顶点都被标记为已访问。
# 迪杰斯特拉算法可以用来解决带权有向图或无向图的最短路径问题。该算法时间复杂度为O(V^2)，其中V为顶点的数量。

def Dijkstra(G, v0, INF=999):  # 999表示该结点到起始点的距离还没有一个确切的值
    dis = dict((i, INF) for i in G.keys())  # 初始化一个距离表，这个表记录着起始结点v0到图中各个点的距离(为inf）
    current = v0  # 一开始，当前点设置为起始点v0
    dis[v0] = 0  # 初始点到自己的距离自然为0
    visited = []  # 用来记录已经遍历过的结点，当把所有的结点都存入的时候，算法结束
    ###
    path = dict((i, []) for i in G.keys())  # 初始化一个路径表，这个表记录着起始结点到途中各个点的最短路径
    path[v0] = str(v0)  # 初始点到自己的路径自然为自己
    ###

    while len(G) > len(visited):  # 图的结点还没被遍历完时执行循环以继续遍历
        visited.append(current)  # 当前点正在被遍历，所以把当前点放入visited表中
        for k in G[current]:  # 遍历当前点的所有相邻点
            if dis[current] + G[current][k] < dis[k]:  # 如果（起始点到当前点的距离+当前点到相邻点k的距离）小于（起始点到当前点的相邻点k的距离）
                dis[k] = dis[current] + G[current][k]  # 则（起始点到当前点的相邻点k的距离）更新为（起始点到当前点的距离+当前点到相邻点k的距离）
                seq = (path[current], str(k))  # 更新路径
                sym = '-'
                path[k] = sym.join(seq)  # 起始点到（当前点的相邻点k）的最短路径，以'-'来连接seq中的两个字符串
        # 接着来选下一个当前点(current)
        # 从剩下未遍历的点中，选取与当前点的距离最小的那个点作为下一个当前点
        new = INF
        for node in dis.keys():
            if node in visited:
                continue
            if dis[node] < new:
                new = dis[node]
                current = node

    return dis, path


v0 = 1
dis, path = Dijkstra(G, v0)
print("%s 到各个结点的最短距离：" % (str(v0)), dis)
print("最短路径为：", path)
