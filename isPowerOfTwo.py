class Solution(object):
	def isPowerOfTwo(self,n):
		if n < 0:
			return False
		else:
			return not(n & n-1)
