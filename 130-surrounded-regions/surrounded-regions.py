class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # same as islands with the condition of not being on the edge!
        rows = len(board)
        columns = len(board[0])

        def dfs(r, c):

            if r < 0 or r > (rows - 1) or c < 0 or c > (columns - 1):
                return

            if board[r][c] == "X" or board[r][c] == "safe":
                return

            if board[r][c] == "O":
                board[r][c] = "safe"
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(columns):
                if r == 0 or r == (rows - 1) or c == 0 or c == (columns - 1):
                    dfs(r, c)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "safe":
                    board[r][c] = "O"


    