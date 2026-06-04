class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]

            # move i while the next number is consecutive
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))

            i += 1

        return res