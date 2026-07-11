class Solution:
    def pacificAtlantic(self, heights):
        result = []
        pacific_set = set()
        atlantic_set = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs_pac(row, col, min):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if heights[row][col] >= min and (row, col) not in pacific_set:
                pacific_set.add((row, col))
            else:
                return

            dfs_pac(row - 1, col, heights[row][col])
            dfs_pac(row + 1, col, heights[row][col])
            dfs_pac(row, col - 1, heights[row][col])
            dfs_pac(row, col + 1, heights[row][col])

            return

        def dfs_atl(row, col, min):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if heights[row][col] >= min and (row, col) not in atlantic_set:
                atlantic_set.add((row, col))
            else:
                return

            dfs_atl(row - 1, col, heights[row][col])
            dfs_atl(row + 1, col, heights[row][col])
            dfs_atl(row, col - 1, heights[row][col])
            dfs_atl(row, col + 1, heights[row][col])

            return

        # Go across pacific border first
        for i in range(cols):
            dfs_pac(0, i, 0)
            dfs_atl(rows - 1, i, 0)
        
        for i in range(rows):
            dfs_pac(i, 0, 0)
            dfs_atl(i , cols - 1, 0)
        
        for item in pacific_set:
            if item in atlantic_set:
                result.append([item[0], item[1]])

        return result
        


        


            