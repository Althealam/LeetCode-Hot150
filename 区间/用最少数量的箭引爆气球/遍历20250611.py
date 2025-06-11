# 思路：
# 1. 将points按照左边界升序排序
# 2. 遍历points的每个相邻区间
# （1）如果第一个区间的右边界大于等于第二个区间的左边界：可以使用同一个箭头，更新第二个区间的边界值
# （2）如果第一个区间的右边界小于第二个区间的左边界：不用同一个箭头，箭头数量加1

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result=0 # 可以使用的最少的箭头数
        points.sort(key=lambda x: x[0]) # 按照第一个元素升序排序
        for i in range(1, len(points)):
            if points[i][0]<=points[i-1][1]: # 第一个区间的右边界大于等于第二个区间的左边界
                points[i][1]=min(points[i][1], points[i-1][1])
            else:
                result+=1
        return result+1