# 1. dp数组以及下标的含义：dp[i]表示凑成金额为i-1时的最少硬币个数
# 2. 递推公式：
# （1）使用coin：dp[i-coin]+1
# （2）不使用coin：dp[i]
# 3. 初始化：全部初始化为inf
# 4. 遍历顺序：先物品后背包（一维数组，并且是01背包）
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j]=min(dp[j], dp[j-coin]+1)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]