class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap = {}

        def dp(start, end):
            if (start, end) in hashmap:
                return hashmap[(start, end)]

            if start > end:
                return 0

            if start == end:
                return nums[start]

            maximum = max(nums[start] + dp(start + 2, end), dp(start + 1, end))

            hashmap[(start, end)] = maximum
            return maximum

        return dp(0, len(nums) - 1)
