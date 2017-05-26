class Solution(object):
	def threeSum(self,nums):
		a = []
		answer = []
		nums.sort(reverse=True)
		for i in range(len(nums)-1):
			if nums[i] == nums[i+1]:
				continue
			for j in range(i+1,len(nums)):
				if j < len(nums)-1 :
					if nums[j] == nums[j+1]:
						continue
				if (-nums[i]-nums[j] in a):
						answer.append([-nums[i]-nums[j],nums[i],nums[j]])
			a.append(nums[i])
		return answer
