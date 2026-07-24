class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative = False
        digits = set("0123456789")
        number = ""

        first_number_yet = False
        sign_seen = False

        for char in s:
            # Spaces are allowed only before the sign or number
            if char == " " and not first_number_yet and not sign_seen:
                continue

            # One optional sign is allowed
            elif char in "+-" and not first_number_yet and not sign_seen:
                sign_seen = True

                if char == "-":
                    is_negative = True

            # Read every digit, including leading zeroes
            elif char in digits:
                number += char
                first_number_yet = True

            # Stop at the first invalid character
            else:
                break

        if number == "":
            return 0

        number = int(number)

        if is_negative:
            number = -number

        return max(-(2 ** 31), min(number, (2 ** 31) - 1))