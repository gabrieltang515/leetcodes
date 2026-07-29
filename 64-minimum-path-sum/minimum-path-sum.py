class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        hashmap = {}

        def dp(row, col):
            if (row, col) in hashmap:
                return hashmap[(row, col)]
            if row == (rows - 1) and col == (columns - 1):
                return grid[row][col]

            if row < 0 or row >= rows or col < 0 or col >= columns:
                return float('inf')

            minimum = min(dp(row + 1, col), dp(row, col + 1))

            hashmap[(row, col)] = grid[row][col] + minimum

            return grid[row][col] + minimum

        return dp(0, 0)