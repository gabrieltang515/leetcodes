class Solution:
    def rob(self, nums: List[int]) -> int:
        # You can either skip one house, skip two house, skip three house etc...
        hashmap = {}
        
        def rec(index):
            if index >= len(nums):
                return 0

            if index in hashmap:
                return hashmap[index]
            
            if index == len(nums) - 1:
                return nums[-1]

            current = nums[index] + rec(index +2)
            skip_current = rec(index+1)

            number = max(current, skip_current)
            hashmap[index] = number
            return number

        return rec(0)