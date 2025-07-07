# 1. dp数组以及下标的含义：dp[i]表示到第i个房间时可以偷到的最大金额
# 2. 递推公式
# （1）不偷i：dp[i-1]
# （2）偷i：dp[i-2]+nums[i]
# 3. 初始化：全部初始化为0 dp[0]=nums[0] dp[1]=max(nums[0], nums[1])
# 4. 遍历顺序：从前向后遍历
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        if len(nums)==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        