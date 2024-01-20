class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        longest = strs[0]

        for s in strs[1:]:
            common = ""
            for i in range(min(len(s), len(longest))):
                if s[i] == longest[i]:
                    common += s[i]
                else:
                    break

            longest = common

        return longest
