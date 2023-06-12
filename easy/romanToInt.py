class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                return res + values[s[i]]
            if values[s[i]] < values[s[i + 1]]:
                res -= values[s[i]]
            else:
                res += values[s[i]]
