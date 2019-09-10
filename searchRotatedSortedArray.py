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
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid 
            if nums[mid] > nums[start]:
                if nums[mid] < target or nums[start] > target: 
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid] > target or nums[end] < target:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
        
        