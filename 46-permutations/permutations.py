class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(remaining, current):
            if not remaining:
                result.append(current[:])
                return

            for num in remaining:
                current.append(num)

                new_remaining = remaining[:]
                new_remaining.remove(num)

                backtracking(new_remaining, current)

                current.pop()

        backtracking(nums, [])
        return result