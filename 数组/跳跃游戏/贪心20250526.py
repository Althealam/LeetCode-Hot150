# 思路：
# 1. 遍历数组nums，获取目前位置可以跳跃达到的最大位置max_cover=max(max_cover, i+nums[i])
# 2. 每次跳跃的时候都判断当前的i是否在max_cover返回内，如果不在的话则返回False
# 3. 如果max_cover>=len(nums)-1，那么就返回True
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_cover=0
        for i in range(len(nums)):
            if i<=max_cover:
                max_cover=max(max_cover, i+nums[i])
            else:
                return False
        return True
