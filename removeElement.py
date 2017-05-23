class Solution(object):
	def removeElement(self,nums,val):
		j = 0; 
		for i in range(len(nums)):
			if nums[i] == val:
				continue;
			nums[j]=nums[i];
			j=j+1; 
		return j;
