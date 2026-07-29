from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = [False] * n

        # min_distance[i] =
        # cheapest cost currently known to connect point i to the MST
        min_distance = [float("inf")] * n
        min_distance[0] = 0

        total_cost = 0

        for _ in range(n):
            current = -1

            # Find the cheapest unvisited point
            for i in range(n):
                if not visited[i]:
                    if current == -1 or min_distance[i] < min_distance[current]:
                        current = i

            # Add this point to the MST
            visited[current] = True
            total_cost += min_distance[current]

            x1, y1 = points[current]

            # Update the cheapest connection for every unvisited point
            for next_point in range(n):
                if not visited[next_point]:
                    x2, y2 = points[next_point]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    min_distance[next_point] = min(
                        min_distance[next_point],
                        distance
                    )

        return total_cost