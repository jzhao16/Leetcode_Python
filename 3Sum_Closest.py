class Solution(object):
	def threeSumClosest(self,nums,target):
		nums.sort()
		dist = [abs(max(nums)*3) + abs(target), 0]
		dist_f =  abs(max(nums)*3) + abs(target)
		for i in range(len(nums)-2):
			if i > 0 and nums[i] == nums[i-1] :
				continue
			j = i + 1
			k = len(nums)-1
			while j < k:
				if (nums[i] + nums[j] +nums[k] == target):
					dist[0] = 0
					break
				elif nums[i] + nums[j] + nums[k] > target:
					temp_dist = nums[i] + nums[j] +nums[k] - target
					if temp_dist <= dist[0]:
						dist = [temp_dist,1]
					k -= 1
				else:
					temp_dist = target - (nums[i] + nums[j] +nums[k])
					if temp_dist <= dist[0]:
						dist = [temp_dist,-1]
					j += 1
			if dist[0] == 0:
				return target
				break
			else:
				dist_f = min(dist_f, dist[0])
		return  dist_f*dist[1] + target				
