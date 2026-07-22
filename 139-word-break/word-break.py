class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        hashmap = {}

        def rec(s, wordDict):
            if s in wordDict:
                return True

            if s in hashmap:
                return hashmap[s]
            
            result = False
            for i in range(len(s)):
                left = s[0:i+1]
                right = s[i+1:]
                if left in wordDict:
                    recursion = rec(right, wordDict)
                    result = result or recursion
                    hashmap[left] = True
                    hashmap[right] = recursion

            return result
        
        return rec(s, wordDict)