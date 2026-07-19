class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking(to_append, candidates, target, index):
            if candidates == []:
                return 
            
            if target == 0:
                result.append(to_append[:])
                return
            elif target < 0:
                return
            
            for i in range(index, len(candidates)):
                integer = candidates[i]   
                if integer <= target:
                    to_append.append(integer)
                else:
                    continue

                backtracking(to_append, candidates, target - integer, i)

                to_append.pop()

        backtracking([], candidates, target, 0)
        return result
            
                