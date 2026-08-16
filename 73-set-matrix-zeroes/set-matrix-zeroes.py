class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        no_of_rows = len(matrix)
        no_of_columns = len(matrix[0])

        for i in range(no_of_rows):
            for j in range(no_of_columns):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for row in list(rows):
            for col in range(no_of_columns):
                matrix[row][col] = 0

        for col in list(columns):
            for row in range(no_of_rows):
                matrix[row][col] = 0

        return matrix
        