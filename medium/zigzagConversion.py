class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        rows = ["" for _ in range(0, numRows)]

        i = 0
        j = 0
        while i < len(s):
            if j == numRows - 1:
                while j > 0 and i < len(s):
                    rows[j] += s[i]
                    i = i + 1
                    j = j - 1
                continue

            rows[j] += s[i]
            i = i + 1
            j = j + 1

        return "".join(rows)
