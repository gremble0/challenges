class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sums = []
        nums_len = len(nums)
        
        for i in range(0, nums_len):
            for j in range(i, nums_len):
                for k in range(j, nums_len):
                    if (nums[i] + nums[j] + nums[k]) == 0 and i != j and i != k and j != k:
                        current = sorted([nums[i], nums[j], nums[k]])
                        if current not in sums:
                            sums.append(current)

        return sums
