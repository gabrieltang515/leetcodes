class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap = {}
        length = len(nums)

        if length == 1:
            return nums[0]
        
        def dp(start, end):
            if (start, end) in hashmap:
                return hashmap[(start, end)]

            if start == end:
                return nums[start]

            if start > end:
                return 0

            # 3 left, can only take middle

            maximum = max(nums[start] + dp(start + 2, end), dp(start + 1, end))

            hashmap[(start, end)] = maximum

            return maximum

        return max(dp(0, length - 2), dp(1, length - 1))