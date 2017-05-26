class Solution(object):
	def twoSum(self,nums,target):
		dict = {}
		for i in range(len(nums)):
			if target - nums[i] in dict:
				return [dict[target-nums[i]],i]
			else:
				dict[nums[i]] = i