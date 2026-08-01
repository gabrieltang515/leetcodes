class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        hashmap = {}
        max_dp = [0] * length
        min_dp = [0] * length

        def dp(i):
            if i == 0:
                max_dp[i] = nums[i]
                min_dp[i] = nums[i]
                return

            max_dp[i] = max(nums[i], nums[i] * max_dp[i - 1], nums[i] * min_dp[i - 1])
            min_dp[i] = min(nums[i], nums[i] * max_dp[i - 1], nums[i] * min_dp[i - 1])

        maximum = -float('inf')

        for i in range(length):
            dp(i)
            maximum = max(maximum, max_dp[i])

        return maximum



            