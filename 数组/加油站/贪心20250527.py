class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果sum(gas)<sum(cost)，说明不管从哪里出发都没办法跑完全程
        if sum(gas)<sum(cost):
            return -1
        # 计算每个站的油耗
        res=[0]*len(gas)
        for i in range(len(gas)):
            res[i]=gas[i]-cost[i]
        sum_=0 # 计算目前的剩余油量
        ans=0 # 记录开始的出发位置
        for i in range(len(res)):
            sum_+=res[i] # 遍历的时候加上当前剩下的油量，确保sum_>0
            if sum_<0:
                ans=i+1 # 从下一个位置作为出发位置
                sum_=0
        return ans
        
        