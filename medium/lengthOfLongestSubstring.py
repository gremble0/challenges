class Solution(object):
    # Rolling window
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = ""
        current_length = 0
        longest_length = 0
        for c in s:
            if not c in current:
                current += c
                current_length += 1
                longest_length = max(current_length, longest_length)
            else:
                i = 0
                while current[i] != c:
                    current = current[1:]
                current = current[1:]
                current += c
                current_length = len(current)
                longest_length = max(current_length, longest_length)

        return longest_length
