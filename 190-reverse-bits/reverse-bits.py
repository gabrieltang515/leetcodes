class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []

        def decimal_to_binaryarray(n):
            while n > 0:
                remainder = n % 2
                result.append(str(remainder))
                n //= 2

            while len(result) < 32:
                result.append("0")

        def binary_to_decimal(binary_array):
            result = 0
            power = 0

            for i in range(len(binary_array) - 1, -1, -1):
                result += int(binary_array[i]) * (2 ** power)
                power += 1
            
            return result

        decimal_to_binaryarray(n)

        return binary_to_decimal(result)

        
