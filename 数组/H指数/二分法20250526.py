# 题意：需要找到一个值h，使得有h篇论文的引用次数至少为h的最大值（小于等于h的所有值x都满足这个性质，而大于h的值都不满足这个性质）
# 每次在查找范围中选择中点mid，同时扫描整个数组，是否有mid个数大于mid。如果有的话，则说明要寻找的h在搜索区间的右边，否则在左边
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 左闭右开区间：[left, right)
        left=0
        right=len(citations)
        while left<right:
            mid=(left+right+1)>>1
            cnt=0
            for v in citations:
                if v>=mid:
                    cnt+=1
            if cnt>=mid:
                # 要找的答案在[mid, right]区间内
                left=mid
            else:
                # 要找的答案在[left, mid-1]区间内
                right=mid-1
        return left