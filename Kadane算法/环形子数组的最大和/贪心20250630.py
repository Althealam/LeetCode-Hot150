# 思路：
# 1. 最大子数组不成环：首尾不相连
# 2. 最大子数组成环：首尾相连，也就是说子数组的一部分在首部，一部分在尾部，因此可以将这种情况转化为第一种情况，也就是求出子数组中最小子数组和，然后将数组之和减去最小子数组和
# 去判断最大子数组成环和不成环时的最大子数组和的最大值
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 1. 求解不成环的情况
        max_sum = float('-inf')
        count = 0
        for i in range(len(nums)):
            count+=nums[i]
            max_sum = max(max_sum, count)
            if count<0:
                count = 0
        
        # 2. 求解成环的情况
        min_sum = 0
        count = 0 
        for i in range(len(nums)):
            count+=nums[i]
            min_sum = min(min_sum, count)
            if count>0:
                count=0

        # 注意：当数组全部为负数时会出现问题，则直接返回max_sum即可
        if sum(nums)==min_sum:
            return max_sum
        return max(max_sum, sum(nums)-min_sum)