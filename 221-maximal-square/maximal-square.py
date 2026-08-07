class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Extra row and column avoid boundary checks
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == "1":
                    dp[row][col] = 1 + min(
                        dp[row - 1][col],      # top
                        dp[row][col - 1],      # left
                        dp[row - 1][col - 1]   # diagonal
                    )
                    max_side = max(max_side, dp[row][col])

        # The problem asks for area, not side length
        return max_side * max_side