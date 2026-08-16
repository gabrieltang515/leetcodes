class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        hashmap = {}

        def dp(row, column):
            
            if (row, column) in hashmap:
                return hashmap[(row, column)]

            if row == m - 1 and column == n - 1:
                return 1

            if row < 0 or row >= m or column < 0 or column >= n:
                return 0

            down = dp(row + 1, column)
            right = dp(row, column + 1)
            hashmap[(row, column)] = down + right
            return hashmap[(row, column)]

        return dp(0, 0)
