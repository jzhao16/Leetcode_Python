class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sub_max = nums[0]
        sub_sum = nums[0]
        for i in range(1, len(nums)):
            sub_sum += nums[i]
            sub_max = max(sub_max, sub_sum, nums[i])
            sub_sum = max(sub_sum, nums[i])
        return sub_max