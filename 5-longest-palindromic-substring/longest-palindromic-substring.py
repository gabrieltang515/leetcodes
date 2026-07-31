class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        # dp[i][j] is True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        longest_start = 0
        longest_length = 1

        # Check substrings from shortest to longest
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = True

                elif length == 2:
                    dp[i][j] = s[i] == s[j]

                else:
                    dp[i][j] = (
                        s[i] == s[j]
                        and dp[i + 1][j - 1]
                    )

                if dp[i][j] and length > longest_length:
                    longest_start = i
                    longest_length = length

        return s[longest_start:longest_start + longest_length]