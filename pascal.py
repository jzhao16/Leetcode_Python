class Solution(object):
	def generate(self,numRows):
		array = [[1]*(i+1) for i in range(numRows)]
		for i in range(numRows):
			for j in range(1,i):
				array[i][j]=array[i-1][j-1]+array[i-1][j]
		return array
