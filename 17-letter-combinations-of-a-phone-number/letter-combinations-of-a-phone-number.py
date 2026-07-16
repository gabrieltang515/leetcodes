class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtracking(index, currentCombination):

            if index == len(digits):
                result.append(currentCombination)
                return

            currentDigit = digits[index]

            for letter in phoneMap[currentDigit]:
                currentCombination = currentCombination + letter
                backtracking(index + 1, currentCombination)
                currentCombination = currentCombination[:index]

            
        backtracking(0, "")
        return result
