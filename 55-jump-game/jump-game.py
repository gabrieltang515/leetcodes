class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex = len(nums) - 1
        furthest = 0
        if len(nums) == 1:
            return True
        
        for i in range(lastindex):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
            if furthest >= lastindex:
                return True

        return False
