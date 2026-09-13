class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        hashmap = {}
        islands = 0

        def dp(row, col):

            if (row, col) in hashmap:
                return 

            if row < 0 or row >= rows or col < 0 or col >= columns:
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            hashmap[(row, col)] = True

            dp(row, col + 1)
            dp(row, col - 1)
            dp(row + 1, col)
            dp(row - 1, col)



        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    islands += 1
                    dp(r, c)


        return islands

            