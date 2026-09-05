class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            sum_without_carry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK

            a = sum_without_carry
            b = carry

        # Convert unsigned 32-bit result into a negative Python integer
        return a if a <= MAX_INT else ~(a ^ MASK)