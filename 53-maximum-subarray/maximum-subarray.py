class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        hashmap = {}

        def dp(i):
            if i == 0:
                return nums[0]

            if i in hashmap:
                return hashmap[i]

            hashmap[i] = max(
                nums[i],              # Start a new subarray
                nums[i] + dp(i - 1)   # Extend the previous subarray
            )

            return hashmap[i]

        maximum = nums[0]

        for i in range(len(nums)):
            maximum = max(maximum, dp(i))

        return maximum