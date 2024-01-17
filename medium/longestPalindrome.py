class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        iter = ""

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                iter += s[j]

                if iter == iter[::-1] and len(iter) >= len(longest):
                    longest = iter

            iter = ""

        return longest
