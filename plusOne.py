class Solution(object):
	def plusOne(self,digits):
		num = 0
		for i in range(len(digits)):
			num = num*10 + digits[i]
		return [int(j) for j in str(num+1)]
