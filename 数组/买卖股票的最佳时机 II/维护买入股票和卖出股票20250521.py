# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 定义两个状态记录买入和卖出股票时的最大值
        sell=0 # 卖出股票的状态
        buy=float('-inf') # 买入股票的状态
        for price in prices:
            sell=max(sell, buy+price) # 变成sell
            buy=max(buy, sell-price) # 变成buy
        return sell