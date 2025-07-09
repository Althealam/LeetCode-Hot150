# 1. dp数组以及下标的含义：
# dp[i][0]表示第i天第一次持有股票的最大收益
# dp[i][1]表示第i天第一次不持有股票的最大收益
# dp[i][2]表示第i天第二次持有股票的最大收益
# dp[i][3]表示第i天第二次不持有股票的最大收益
# dp[i][j]表示第i天第j%2次持有股票的最大收益（j%2==0）
# dp[i][j]表示第i天第j%2次不持有股票的最大收益（j%2!=0）
# 2. 递推公式
# （1）dp[i][0] = max(dp[i-1][0], -prices[i])
# （2）dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i]) （j%2==0）
# （3）dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i]) （j%2!=0）
# 3. 初始化：dp[0][j]=-prices[0] j%2==0
# 4. 遍历顺序：从左到右遍历prices
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=[[0]*2*k for _ in range(len(prices))]
        for j in range(2*k):
            if j%2==0:
                dp[0][j]=-prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            for j in range(2*k):
                if j==0:
                    dp[i][j] = max(dp[i-1][j], -prices[i])
                elif j%2==0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        
        return dp[-1][-1]
