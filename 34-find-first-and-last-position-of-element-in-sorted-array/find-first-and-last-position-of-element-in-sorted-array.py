class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1

        result = []

        leftmost = -1
        rightmost = -1 

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                leftmost = mid
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                rightmost = mid
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1


        return [leftmost, rightmost]