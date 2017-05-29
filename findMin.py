class Solution(object):
	def findMin(self,nums):
		left = 0
		right = len(nums)-1
		while right - left > 1 and nums[left] > nums[right] :
			mid = int(( left + right )/2)
			if nums[left] < nums[mid]:
				left = mid
			else:
				right = mid
		if nums[left] < nums[right]:
			return nums[left]
		else:
			return nums[right]
