# 思路：
# 1. 将区间按照左边升序排序
# 2. 将第一个区间放入到res中
# 3. 遍历intervals剩下的区间，判断当前遍历的区间的左边界和res最后一个区间的右边界，如果重合的话则弹出res中的最后一个区间，更新区间的值并加入
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # 按照左边的边界进行排序
        res=[intervals[0]] # res存放合并区间后的结果值
        for i in range(1, len(intervals)):
            if res[-1][1]>=intervals[i][0]: # res最后一个区间的右边界大于等于当前遍历区间的左边界 
                intervals[i][0]=min(res[-1][0], intervals[i][0])
                intervals[i][1]=max(res[-1][1], intervals[i][1])
                res.pop() # 弹出元素
            res.append(intervals[i])
        return res

