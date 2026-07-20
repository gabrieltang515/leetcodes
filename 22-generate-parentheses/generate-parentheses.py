class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(to_append, open, close):
            if len(to_append) == (2 * n):
                if "".join(to_append) not in result:
                    result.append("".join(to_append))
                return

            if open < n:
                to_append.append("(")
                backtracking(to_append, open + 1, close)
                to_append.pop()
            
            if close < open:
                to_append.append(")")
                backtracking(to_append, open, close + 1)
                to_append.pop()

        backtracking([], 0, 0)
        return result