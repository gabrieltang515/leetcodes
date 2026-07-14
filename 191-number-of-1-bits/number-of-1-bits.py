class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        set_bits = 0

        while n > 0:
            remainder = n % 2
            if remainder == 1:
                set_bits += 1
            n //= 2

        return set_bits
