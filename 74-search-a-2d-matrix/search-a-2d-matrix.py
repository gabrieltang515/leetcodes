class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            first = matrix[i][0]
            last = matrix[i][-1]

            if target < first or target > last:
                continue

            left = 0
            right = columns - 1

            while left <= right:
                mid = (left + right) // 2

                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return False