class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {1:1, 2:2}

        def rec(n):
            if n in hashmap:
                return hashmap[n]
            else: 
                result = rec(n-1) + rec(n-2)
                hashmap[n] = result
                return result

        return rec(n)