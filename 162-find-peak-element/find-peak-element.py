class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            if mid == len(nums) - 1:
                return mid
            
            if left == right:
                return mid

            if mid == 0 and nums[mid] > nums[mid+1]:
                return 0

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1 
            elif nums[mid] > nums[mid + 1]:
                right = mid - 1


        