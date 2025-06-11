# 思路：
# 假设我们此时遍历到区间[li, ri]
# 1. 如果ri<left，说明[li, ri]与S不重叠并且在其左侧，因此可以直接将[li, ri]加入答案
# 2. 如果li>right，说明[li, ri]与S不重叠并且在其右侧，因此可以直接将[li, ri]加入答案
# 3. 如果上面的情况都不满足，说明[li, ri]与S重叠，因此不用将[li, ri]加入答案。此时将S与[li, ri]合并，也就是将S更新为其与[li, ri]的并集

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval # 左右区间
        ans=[] # 答案值
        insert=False # 是否插入
        for interval in intervals: # 遍历区间的左右边界
            interval_left, interval_right = interval
            if interval_right<left: # 当前遍历的区间的右边界小于待插入的区间的左边界==>该区间在待插入区间的左边==>先插入当前区间
                ans.append(interval)
            elif interval_left>right: # 当前遍历的区间的左边界大于待插入的区间的右边界==>该区间在待插入区间的右边==>先插入待插入区间
                if not insert:
                    ans.append([left, right])
                    insert=True
                ans.append(interval)
            else:
                # 当前遍历的区间和待插入区间重合
                left = min(left, interval_left)
                right = max(right, interval_right)

        # 如果待插入区间在所有区间的右边   
        if not insert:
            ans.append([left, right])
        return ans
