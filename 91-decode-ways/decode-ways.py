class Solution:
    def numDecodings(self, s: str) -> int:
        hashmap = {}

        def dp(start):
            # Reaching the end means one valid decoding was completed
            if start == len(s):
                return 1

            # No letter maps to a number beginning with 0
            if s[start] == "0":
                return 0

            if start in hashmap:
                return hashmap[start]

            # Option 1: Decode one digit
            ways = dp(start + 1)

            # Option 2: Decode two digits
            if (
                start + 1 < len(s)
                and 10 <= int(s[start:start + 2]) <= 26
            ):
                ways += dp(start + 2)

            hashmap[start] = ways
            return ways

        return dp(0)