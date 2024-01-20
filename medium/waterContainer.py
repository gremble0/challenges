class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)
        highest = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            highest = max(highest, area)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1

        return highest
