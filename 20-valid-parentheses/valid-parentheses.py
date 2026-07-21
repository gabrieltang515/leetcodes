class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            "(": ")",
            "[":"]",
            "{":"}"
        }

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if stack != [] and mapping[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return stack == []