# 思路：
# 假设我们此时遍历到区间[li, ri]
# 1. 如果ri<left，说明[li, ri]与S不重叠并且在其左侧，因此可以直接将[li, ri]加入答案
# 2. 如果li>right，说明[li, ri]与S不重叠并且在其右侧，因此可以直接将[li, ri]加入答案
# 3. 如果上面的情况都不满足，说明[li, ri]与S重叠，因此不用将[li, ri]加入答案。此时将S与[li, ri]合并，也就是将S更新为其与[li, ri]的并集

# 方法二：将新区间加入到区间列表中，然后按照区间合并的常规方法进行合并
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals):
            intervals.sort(key=lambda x: x[0]) # 按照左区间排序
            ans=[intervals[0]]
            for i in range(1, len(intervals)):
                if ans[-1][1]>=intervals[i][0]:
                    intervals[i][1]=max(ans[-1][1], intervals[i][1])
                    intervals[i][0]=min(ans[-1][0], intervals[i][0])
                    ans.pop()
                ans.append(intervals[i])
            return ans
        intervals.append(newInterval)
        result_interval=merge(intervals)
        return result_interval
                    

            

            
