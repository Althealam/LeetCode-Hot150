# 思路：定义left和right，计算left到right区间内的元素值sum_

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum_=0
        result=float('inf')
        while right<len(nums):
            sum_+=nums[right]
            while sum_>=target:
                result=min(result, right-left+1)
                sum_-=nums[left]
                left+=1
            right+=1
        return result if result!=float('inf') else 0