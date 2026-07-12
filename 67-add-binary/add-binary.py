class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []

        a_ptr = len(a) - 1
        b_ptr = len(b) - 1
        carry = 0

        while a_ptr >= 0 or b_ptr >= 0:
            if a_ptr >= 0 and b_ptr >= 0:
                sum = int(a[a_ptr]) + int(b[b_ptr]) + carry
            elif a_ptr >= 0:
                sum = int(a[a_ptr]) + carry
            elif b_ptr >= 0:
                sum = int(b[b_ptr]) + carry

            carry = 0
            if sum == 2:
                carry = 1
                sum = 0
            elif sum == 3:
                carry = 1
                sum = 1

            result.append(str(sum))
            a_ptr -= 1
            b_ptr -= 1
        
        if carry != 0:
            result.append(str(carry))
        result.reverse()
        return "".join(result)
