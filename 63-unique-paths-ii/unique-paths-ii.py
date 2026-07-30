class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        hashmap = {}

        def dp(row, col):
            # Out of bounds
            if row >= rows or col >= columns:
                return 0

            # Obstacle
            if obstacleGrid[row][col] == 1:
                return 0

            # Reached destination
            if row == rows - 1 and col == columns - 1:
                return 1

            if (row, col) in hashmap:
                return hashmap[(row, col)]

            paths_down = dp(row + 1, col)
            paths_right = dp(row, col + 1)

            hashmap[(row, col)] = paths_down + paths_right
            return hashmap[(row, col)]

        return dp(0, 0)