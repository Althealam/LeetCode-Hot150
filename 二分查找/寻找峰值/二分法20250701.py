# 思路：二分法
# 使用开区间(-1, n-1)，不使用闭区间是因为如果峰值是n-1的话，那么nums[0]<nums[1]<...<nums[n-1]，那么数组是单调递增的，不符合题目含义

# 时间复杂度：O(logn)
# 空间复杂度：O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = -1, len(nums)-1 # 开区间：(-1, n-1)
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                right = mid # 峰值在(left, mid)中
            else:
                left = mid # 峰值在(mid+1, right)中
        return right
