# 位置i能够达到的水柱高度和其左边的最高柱子以及右边的最高柱子有关，分别称这两个柱子的高度为left_max, right_max；位置i最大的水柱高度就是max(left_max, right_max)
# 栈内存储的是还没计算出水柱高度的元素的下标，并且该单调栈的栈顶元素是最大的，也就是说单调栈是单调递增的（从栈底到栈顶）
# 思路：
# 1. 定义一个单调栈，存储还没计算出水柱高度的元素的下标
# 2. 遍历heights，如果该元素比栈顶元素的值大，说明找到了栈顶元素的right_max，那么left_max就是弹出栈顶元素后的栈顶元素
# 3. 求出栈顶元素的水柱高度：min(height[left_max], height[right_max])-bottom_h（其中bottom_h就是栈顶元素的高度）
# 4. 求出水柱的宽度：i-left_max-1 

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        stack=[] # 栈中存储还没计算出水柱高度的的元素的下标
        for i in range(len(height)): # 判断当前遍历元素是否是栈顶元素的right_max
            while stack and height[i]>=height[stack[-1]]: # 当前元素是栈顶元素的right_max
                right_max=i # 右边的最高水柱
                bottom_height=height[stack.pop()] # 弹出栈顶元素，计算最底部的柱子高度
                if len(stack)==0:
                    break
                left_max=stack[-1] # 左边的最高水柱
                h=min(height[left_max], height[right_max])-bottom_height # 水柱高度
                l=i-left_max-1 # 水柱宽度
                ans+=h*l # 计算当前的栈顶元素的水柱高度
            stack.append(i) 
        return ans
