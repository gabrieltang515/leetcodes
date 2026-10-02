class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_product = []

        suffix_product = []

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            prefix = prefix * nums[i]
            prefix_product.append(prefix)

        for i in range(len(nums) - 1, -1, -1):
            suffix = suffix * nums[i]
            suffix_product.append(suffix)

        suffix_product.reverse()

        answer = []

        for i in range(len(nums)):
            if i == 0:
                answer.append(suffix_product[1])
                continue

            if i == len(nums) - 1:
                answer.append(prefix_product[len(nums) - 2])
                continue

            to_append = prefix_product[i - 1] * suffix_product[i + 1]
            answer.append(to_append)

        return answer



        