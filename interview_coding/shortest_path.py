class Solution:
    def short_path(self, G, v0):
        min_path = {i:float('inf') for i in G}
        min_path[v0] = 0

        for item in G[v0]:
            G[v0][item] + self.short_path(G, item)



if __name__ == '__main__':
    G = {1:{1:0, 2:1, 3:12},
         2:{2:0, 3:9, 4:3},
         3:{3:0, 5:5},
         4:{3:4, 4:0, 5:13, 6:15},
         5:{5:0, 6:4},
         6:{6:0}}


