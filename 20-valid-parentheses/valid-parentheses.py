class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "{": "}", "[":"]"}

        stack = []

        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if stack == []:
                    return False

                if stack != [] and char == hashmap[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

