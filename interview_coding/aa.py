def distance(G, v, dist, length, M, R):
    if len(R) == 0 or len(G[v]) == 1:
        return

    length += 1
    M.append(v)
    R.remove(v)

    for link_v in G[v].keys():
        if link_v in M:
            continue
        if dist[v] + G[v][link_v] < dist[link_v]:
            dist[link_v] = dist[v] + G[v][link_v]
        distance(G, link_v, dist, length, M, R)


if __name__ == "__main__":
    G = {1: {1: 0, 2: 1, 3: 12},
         2: {2: 0, 3: 9, 4: 3},
         3: {3: 0, 5: 5},
         4: {3: 4, 4: 0, 5: 13, 6: 15},
         5: {5: 0, 6: 4},
         6: {6: 0}}

    v0 = 1
    length = 1
    M = []
    R = [k for k in G.keys()]

    dist = dict((k, 99) for k in G.keys())
    dist[v0] = 0

    distance(G, v0, dist, length, M, R)
    print(dist)