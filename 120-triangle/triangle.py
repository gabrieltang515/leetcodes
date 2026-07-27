class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        hashmap = {}
        def dp(row, column):
            if (row, column) in hashmap:
                return hashmap[(row, column)]

            if row == len(triangle):
                return 0

            minimum = float('inf')
            minimum = min(dp(row + 1, column), dp(row + 1, column + 1))
            hashmap[(row, column)] = triangle[row][column] + minimum
            return triangle[row][column] + minimum

        return dp(0, 0)