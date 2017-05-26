class Solution(object):
	def getRow(self,rowIndex):
		a=[]
		for i in range(rowIndex+1):
			for j in range (i-1,0,-1):
				a[j] = a[j-1] + a[j]
			a.append(1)
		return a
