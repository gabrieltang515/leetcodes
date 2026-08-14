class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_length = len(text1)
        text2_length = len(text2)

        matrix = [[-1] * (text2_length) for _ in range(text1_length)]

        # i and j are the 
        def dp(i, j): 
            if i < 0 or j < 0:
                return 0

            if matrix[i][j] != -1:
                return matrix[i][j]
            elif text1[i] == text2[j]:
                matrix[i][j] = dp(i - 1, j - 1) + 1
            else:
                matrix[i][j] = max(dp(i - 1, j), dp(i, j - 1))

            return matrix[i][j]
        
        return dp(text1_length - 1, text2_length - 1)
        