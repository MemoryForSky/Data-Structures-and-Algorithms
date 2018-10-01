
"""
Dijkstra 算法：
计算指定点 v0 到图 G 中任意点的最短路径的距离

基本思想：
(1) 每次找到离源点最近的一个顶点，然后以该顶点为中间点进行扩展；
(2) 最终得到源点到其余所有点的最短路径；
(3) 该算法是一种贪婪算法

其中：
INF 为设定的无限远距离值
此方法不能解决负权值边的图
"""

def Dijkstra(G, v0, INF=999):
    # S为已求出最短路径的顶点集合
    S = set()
    minv = v0
    # 源顶点到其余各顶点的初始路程
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0

    while len(S) < len(G):
        # minv设为中间点
        S.add(minv)

        # 从中间点minv开始向后找：找到最短距离并更新距离字典
        for w in G[minv]:
            # 如果dis(开始，中间点) + (中间点，连接点) < 已知最短距离
            if dis[minv] + G[minv][w] < dis[w]:
                # 对已知最短距离进行更新
                dis[w] = dis[minv] + G[minv][w]

        # 从剩下的未确定顶点集合U中选择最小距离点作为新的扩散点
        new_node = INF
        for v in dis.keys():
            # 跳过已确定最短距离的点
            if v in S: continue
            if dis[v] < new_node:
                new_node = dis[v]
                # 求最小距离点，作为新的扩散点
                minv = v
    return dis

if __name__ == '__main__':
    G = {1:{1:0, 2:1, 3:12},
      2:{2:0, 3:9, 4:3},
      3:{3:0, 5:5},
      4:{3:4, 4:0, 5:13, 6:15},
      5:{5:0, 6:4},
      6:{6:0}}

    dis = Dijkstra(G,v0=1)
    for item in dis:
        print("从1点到", item, "点最短距离为：", dis[item])