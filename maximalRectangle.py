class Solution(object):
	def maximalRectangle(self,matrix):
		max_area = 0
		for i in range(len(matrix)):
			height = []
			for j in range(len(matrix[i])):
				count = 0
				while i >=0 and int(matrix[i][j]) == 1:
					count += 1
					i -= 1
				height.append(count)
				i += count 
			max_area = max(max_area, self.largestRectangleArea(height)) 
		return max_area
			
	def largestRectangleArea(self,height):
		if len(height) < 2:
			return height[0] if len(height) else 0
		height.append(0)
		max_area = 0
		for i in range(1, len(height)):
			j = i - 1
			while j >= 0 and height[j] > height[i]:
				max_area = max(max_area,height[j]*(i-j))
				height[j] = height[i]
				j -= 1
		return max_area

