class Solution(object):
	def missingNumber(self, nums):
		x = 0
		for i in range(len(nums)):
			x = x ^ i ^ nums[i]
		return x ^ len(nums) 