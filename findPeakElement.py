class Solution(object):
	def findPeakElement(self, nums):
		if len(nums) == 1:
			return 0
		begin, end = 1, len(nums)-2
		while begin <= end:
			mid = int((begin + end)/2)
			if nums[mid] < nums[mid+1]:
				begin = mid + 1
			else:
				if nums[mid] > nums[mid-1]:
					return mid
				else:
					end = mid - 1
		return nums.index(max(nums[begin],nums[end]))