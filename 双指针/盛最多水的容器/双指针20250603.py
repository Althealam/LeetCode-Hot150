# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1
        while left<right:
            area=(right-left)*min(height[left], height[right]) # 计算面积
            ans=max(ans, area) # 计算最多的面积
            if height[left]<height[right]: # height[left]与右边的任意线段都无法组成一个比ans更大的面积
                left+=1
            else: # height[left]与左边的任意线段都无法组成一个比ans更大的面积
                right-=1
        return ans