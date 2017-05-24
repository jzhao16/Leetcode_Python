class Solution(object):
	def removeDuplicates(self,nums):
		if len(nums) == 0:
			return 0
		elif len(nums) ==1:
			return 1
		else:
			j = 0
			i = 1
			k = 0
			for i in range(1,len(nums)):
				if nums[j] == nums[i]:
					if k < 1:
						j += 1
						nums[j] = nums[i]
						k += 1
						continue
					else:
						continue
				else:
					j +=1
					nums[j] = nums[i]
					k = 0
			return j+1, nums
