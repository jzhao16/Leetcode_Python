class Solution(object):
	def searchRange(self, nums, target):
		range_c = []
		begin , end = 0, len(nums) -1 
		while begin <= end:
			mid = int ((begin + end) / 2)
			mid_value = nums[mid]

			if (mid_value == target):
				i = j = mid
				while  i > 0 and nums[i-1] == target:
					i = i - 1
				range_c.append(i)
				while j < len(nums)-1 and nums[j+1] == target:
					j = j + 1
				range_c.append(j)
				return range_c

			elif (mid_value > target):
				end = mid - 1 
			else:
				begin = mid + 1
		return [-1,-1]
