import io
import sys

#满足以下两个条件才能称为欧拉回路：
#每个节点都必须有相同数量的入度和出度。
#图必须是连通的，也就是说，从任意一个节点出发，可以经过图中的边到达图中的任意其他节点。

class Solution:
    type = 0
    h, ne, e, idx, used, res = None, None, None, None, None, None
    # 加边函数
    def add(self, a: int, b: int):
        self.e[self.idx] = b
        self.ne[self.idx] = self.h[a]
        self.h[a] = self.idx
        self.idx += 1

    # 这里存在很多个自环的数据所以在递归的使用python语言绝对会爆栈
    def dfs(self, u: int):
        i = self.h[u]
        while i != -1:
            # i表示当前是第i条的边, 如果当前第i条边已经用过那么当前节点u的表头跳到u的邻接点上, 也即下一条边
            if self.used[i] == 1:
                # 优化: 修改h[u]可以使得回溯之后往下递归避免很多个自环又遍历重复边的情况
                self.h[u] = self.ne[i]
                i = self.h[u]
                # 跳过当前的边
                continue
            # 标记当前的边已经被访问
            self.used[i] = 1
            if self.type == 1:
                # 因为是无向图所以要标记反向边, 这里使用h, e, ne三个数组来建图有一个好处是非常容易找到反向边, i ^ 1就是i的反向边
                self.used[i ^ 1] = 1
            t = 0
            # 当无向边的时候0-1是一组边, 2-3是一组边, 4-5是一组边...所以边的编号应该是i // 2 + 1
            if self.type == 1:
                t = i // 2 + 1
                # 由题目要求标记反向边, 可以发现i是奇数的时候那么说明当前是反向边
                if i & 1: t = -t
            else:
                # 因为边数是从0开始的, 所以当为有向图的时候i + 1就是当前的第几条边
                t = i + 1
            # j为当前边的终点
            j = self.e[i]
            # 优化: 修改当前节点u的表头跳到下一条边
            self.h[u] = self.ne[i]
            self.dfs(j)
            # 递归完当前节点的邻接点之后加入当前的节点u到欧拉路径的序列中
            self.res.append(t)
            i = self.h[u]

    def process(self):
        self.type = int(input())
        n, m = map(int, input().split())
        self.h, self.e, self.ne, self.used = [-1] * (n + 10), [0] * (m + 10) * 2, [0] * (m + 10) * 2, [0] * (m + 10) * 2
        self.idx = 0
        # 统计一个节点的入度和出度, 这样可以判断是否无解
        din, dout = [0] * (n + 10), [0] * (n + 10)
        for i in range(m):
            a, b = map(int, input().split())
            self.add(a, b)
            # 这里将无向边看成是特殊的有向边
            din[b] += 1
            dout[a] += 1
            # 无向图
            if self.type == 1:
                # 添加反向边
                self.add(b, a)
        if self.type == 1:
            for i in range(1, n + 1):
                # 存在奇数说明节点i出去和进来的边的数量不相等那么不存在欧拉回路
                if din[i] + dout[i] & 1:
                    print("NO")
                    return
        else:
            # 有向图需要满足每一个节点的入度 = 出度
            for i in range(1, n + 1):
                if din[i] != dout[i]:
                    print("NO")
                    return
        self.res = list()
        for i in range(1, n + 1):
            # 表头不空的时候那么往下递归
            if self.h[i] != -1:
                self.dfs(i)
                break
        if len(self.res) < m:
            print("NO")
            return
        print("YES")
        for i in range(len(self.res) - 1, -1, -1):
            print(self.res[i], end=" ")


solution = Solution()
solution.process()
#输入格式：
#第一行包含一个整数 type（0 或 1），表示图的类型（0 表示有向图，1 表示无向图）。
#第二行包含两个以空格分隔的整数 n 和 m，其中 n 表示图中节点的数量，m 表示边的数量。
#接下来的 m 行，每行包含两个以空格分隔的整数 a 和 b，表示从节点 a 到节点 b 存在一条边。