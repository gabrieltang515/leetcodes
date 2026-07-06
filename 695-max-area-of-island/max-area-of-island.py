class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        rows = len(grid)
        columns = len(grid[0])

        def dfs(r, c):
            area = 0
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area += 1

            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)

            return area

        for r in range(rows):
            for c in range(columns):
                max_area = max(dfs(r, c), max_area)

        
        return max_area


