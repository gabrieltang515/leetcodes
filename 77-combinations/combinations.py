class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        result = []

        for i in range(1, n+1):
            nums.append(i)

        def backtracking(k, to_append, nums):

            if k == 0:
                result.append(to_append[:])
                return

            if nums == []:
                return
            
            for i in range(len(nums)):
                to_append.append(nums[i])
                backtracking(k - 1, to_append, nums[i + 1:])
                to_append.remove(nums[i])

        backtracking(k, [], nums)

        return result


