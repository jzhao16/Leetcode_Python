class Solution(object):
	def searchMatrix(self,matrix,target):
		if len(matrix)==0:
			return False
		if len(matrix[0]) == 0:
			return False
		row_number, col_number = len(matrix), len(matrix[0])
		begin , end = 0, row_number * col_number -1 
		while (begin <= end):
			mid = int ((begin + end) / 2)
			mid_value = matrix[int(mid / col_number)][mid % col_number]

			if (mid_value == target):
				return True
			elif (mid_value > target):
				end = mid -1 
			else:
				begin = mid + 1
		return False
