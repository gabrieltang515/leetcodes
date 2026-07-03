class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        hashmap = {}

        for i in range(length + 1):
            hashmap[i] = i

        for num in nums:
            del hashmap[num]

        if hashmap is not None:
            return list(hashmap)[0]

        return 0

            


