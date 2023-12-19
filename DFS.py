def isEuler():
    allVisited = True
    for e in visited:
        if e == 0:
            allVisited = False
    if allVisited:
        if queue[0] == queue[len(queue) - 1]:
            return 1
        else:
            return 2
    return 0


def printPath(flag):
    if flag == 1:
        print("是欧拉回路:", end="")
    else:
        print("是欧拉道路:", end="")
    for i in range(len(queue)):
        if i < len(queue) - 1:
            print(queue[i], "-> ", end="")
        else:
            print(queue[i])


def dfs(x):
    queue.append(x)
    flag = isEuler()
    if flag > 0:
        eulerFlag = True
        printPath(flag)
    for i in range(len(eulerEdges)):
        if visited[i]:
            continue
        visited[i] = 1
        if eulerEdges[i][0] == x:
            dfs(eulerEdges[i][1])
            queue.pop()
            visited[i] = 0
        elif eulerEdges[i][1] == x:
            dfs(eulerEdges[i][0])
            queue.pop()
            visited[i] = 0


eulerEdges = [
    (1, 2),
    (1, 2),
    (1, 0),
    (2, 0),
    (2, 3),
    (2, 3),
    (3, 0)
]
queue = []
visited = [0 for _ in range(len(eulerEdges))]
eulerFlag = False
start = 1

dfs(start)
if not eulerFlag:
    print("不是欧拉回路或欧拉道路")