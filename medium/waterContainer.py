class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def areaBetween(index1, index2):
            return min(height[index1], height[index2]) * (index2 - index1)

        def maxFrom(index):
            max_seen = 0
            for i in range(index, len(height)):
                max_seen = max(max_seen, areaBetween(index, i))

            return max_seen
                
        areas = []
        for i in range(0, len(height)):
            areas.append(maxFrom(i))

        return max(areas)
