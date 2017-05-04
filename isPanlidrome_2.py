class Solution(object):
	def isPalindrome(self,x):
		if x < 0 :
			return False
		elif x == 0 :
			return True
		else :
			rev = 0
			y =x
			while x > 0:
				rev = rev * 10 + (x % 10)
				x = int (x/10)
			if y == rev:
				return True
			else:
				return False
