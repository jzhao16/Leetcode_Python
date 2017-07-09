class Solution(object):
	def isPowerOfTwo(self,n):
		if n > 1:
            while n%2 == 0:
                n /= 2
        return n==1