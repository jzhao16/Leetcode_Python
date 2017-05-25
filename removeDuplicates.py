class Solution(object):
	def removeDuplicates(self, nums):
		if range(len(nums)==0):
			return 0;
		elif range(len(nums)==1):
			return 1;
		else:
			i = 1;
			j = 0;
			for i in range(len(nums)):
				if nums[j] != nums[i]:
					nums[j+1] = nums [i];
					j += 1;
			return j + 1
