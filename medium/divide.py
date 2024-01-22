class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i = 0
        if bool(dividend > 0) == bool(divisor > 0):
            divisor = abs(divisor)
            dividend = abs(dividend)
            if divisor == 1:
                return 1
            while dividend >= divisor:
                print(dividend)
                dividend -= divisor
                i += 1
        else:
            divisor = abs(divisor)
            dividend = abs(dividend)
            if divisor == 1:
                return -1
            while dividend >= divisor:
                dividend -= divisor
                i -= 1

        return i
