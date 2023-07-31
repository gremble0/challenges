class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        length = len(merged)

        if length % 2 == 0:
            return (merged[int(length / 2)] + merged[int(length / 2 - 1)]) / 2
        return float(merged[int(length / 2)])

s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
