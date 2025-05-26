# 题意：给定一个数组，求一个最大h，使得数组中至少有h个数都大于等于h
# 思路：创建一个长度为n+1的cnt数组，统计min(citations[i], n)的出现次数
# 假设s为引用次数>=i的论文数，我们需要算出满足s>=i的最大的i

# 时间复杂度: O(n)
# 空间复杂度: O(n)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        cnt=[0]*(n+1) # 计算每个被引用次数出现的频率
        for c in citations:
            cnt[min(c, n)]+=1 # 被引用频率h不可以超过n
        s=0
        for i in range(n, -1, -1): # i=0的时候 s>=i一定成立（遍历引用次数）
            s+=cnt[i] # 统计
            if s>=i: # 说明有至少i篇论文的引用次数至少为i
                return i

        