class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_y] = root_x
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        for i in range(len(points) - 1):
            point1 = points[i]
            for j in range(i+1, len(points)):
                point2 = points[j]
                manhattan = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

                edges.append((manhattan, i, j))

        cost = 0
        edges.sort()
        connected = []
        uf = UnionFind(len(points))

        for k in range(len(edges)):
            edge = edges[k]

            if len(connected) == len(points):
                return cost

            if uf.find(edge[1]) == uf.find(edge[2]): # connected
                continue
            else:
                connected.append(edge[2])
                uf.union(edge[1], edge[2])
                cost += edge[0]

        return cost



