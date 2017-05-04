class Solution(object):
	def romanToInt(self,s):
		# s is the roman numeral string
		# dict is the roman charater to number dictionary
		dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		z = 0
		for i in range(len(s)-1):
			if dict[s[i]] < dict[s[i+1]]:
				z -= dict[s[i]]
			else:
				z += dict[s[i]]
		z += dict[s[-1]]
		return z