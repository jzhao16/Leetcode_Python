class Solution(object):
	def hammingWeight(self, n):
		while n > 0:
			count += n & 1
			n >> 1
		return count