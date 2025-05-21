# 思路：贪心思路，枚举从左到右卖出价格prices[i]时可以获得的最大利润是多少
# 我们需要知道第i天之前，股票价格的最小值是多少，也就是从prices[0]到prices[i-1]的最小值，把它作为买入价格
# 相当于维护买入的最小价格即可

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min_price=prices[0] # i天前买入的最小价格
        for i in range(len(prices)):
            ans=max(ans, prices[i]-min_price)
            min_price=min(min_price, prices[i])
        return ans
