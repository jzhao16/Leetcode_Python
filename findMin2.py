class Solution(object):
	def findMin(self,nums):
		left = 0
		right = len(nums)-1
		while right - left > 1 and nums[left] >= nums[right] :
			mid = int(( left + right )/2)
			if nums[left] < nums[mid]:
				left = mid
			elif nums[left] > nums[mid]:
				right = mid
			else:
				left += 1
				while left < mid and nums[left] == nums[left+1]:
					left +=1 
		if nums[left] < nums[right]:
			return nums[left]
		else:
			return nums[right]
