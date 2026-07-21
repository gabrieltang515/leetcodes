class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []

        for i in range(len(nums)):
            number = nums[i]

            if number in hashmap:
                hashmap[number] += 1
            else:
                hashmap[number] = 1

        for number in hashmap:
            if hashmap[number] == 2:
                result.append(number)

        return result