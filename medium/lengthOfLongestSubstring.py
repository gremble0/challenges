class Solution(object):
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
                for i in range(0, len(current)):
                    if current[i] == c:
                        current = current[1:]
                        break
                    current = current[1:]
                current += c
                current_length = len(current)
                longest_length = max(current_length, longest_length)
            print(current)

        return longest_length

s = Solution()
print(s.lengthOfLongestSubstring("abbb"))
