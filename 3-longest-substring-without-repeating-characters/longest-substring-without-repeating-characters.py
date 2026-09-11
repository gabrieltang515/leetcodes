class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}

        max_length = 0

        p1 = 0

        for p2 in range(len(s)):

            char = s[p2]

            if char in hashmap and hashmap[char] >= p1:
                p1 = hashmap[char] + 1

            hashmap[char] = p2
            max_length = max(max_length, p2 - p1 + 1)

        return max_length


        