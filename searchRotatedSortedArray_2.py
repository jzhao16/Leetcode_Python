class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while end - 1 > start:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[start]:
                if  nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1