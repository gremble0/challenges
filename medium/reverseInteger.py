class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        as_str = str(x)
        if as_str[0] == "-":
            reversed = -int(as_str[::-1][0:-1])
        else:
            reversed = int(as_str[::-1])

        return reversed if -2 ** 31 < reversed < 2 ** 31 else 0
        
print(Solution().reverse(1534236469))
