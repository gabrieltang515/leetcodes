class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashmap = {}

        # for ele in nums:
        #     if ele in hashmap:
        #         hashmap[ele] = hashmap[ele] + 1
        #     else:
        #         hashmap[ele] = 1

        # for ele in nums:
        #     if hashmap[ele] == 1:
        #         return ele
        xor_sum = 0
        for i in range(len(nums)):
            xor_sum = xor_sum ^ nums[i]

        return xor_sum
            

            