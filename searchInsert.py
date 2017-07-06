class Solution(object):
	def searchInsert(self, nums, target):
		begin , end = 0, len(nums)-1
		while begin <= end :
			mid = int ((begin + end) /2) 
			mid_value = nums[mid]
			if mid_value == target:
				return mid
			elif mid_value < target:
				begin = mid + 1 
			else :
				end = mid - 1
		return begin
