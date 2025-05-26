# 题意：给定一个数组，求一个最大h，使得数组中至少有h个数都大于等于h（这个h是论文的引用次数）
# 思路：将初始的H指数h设置为0，然后将引用次数排序，并且对排序后的数组从大到小遍历
# 如果当前H指数为h并且在遍历过程中找到了当前值citations[i]>h，说明我们至少找到了一篇被引用了至少h+1次的论文，因此将现有的h+1，继续遍历直到h无法继续增大
# 时间复杂度：O(nlogn) 排序需要nlogn
# 空间复杂度：O(logn) 

class Solution:
    def hIndex(self, citations):
        sorted_citations=sorted(citations, reverse=True) # 倒叙排序，需要确保最大的元素在最前面
        h=0
        i=0
        n=len(citations)
        while i<n and sorted_citations[i]>h: # 如果sorted_citations[i]>h，说明目前该论文的引用次数是大于h的
            h+=1
            i+=1
            print("目前遍历的论文引用次数为:",sorted_citations[i])
            print("h:",h)
        return h

citations=[3,0,6,1,5]
sol=Solution()
print(sol.hIndex(citations))