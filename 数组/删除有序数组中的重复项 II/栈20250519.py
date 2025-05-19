# 思路：用一个栈记录去重后的元素，如果当前元素等于栈顶下方的数（倒数第二个数），那么不能入栈（否则会有三个一样的数），反之可以入栈
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack_size=2 # 栈的大小
        for i in range(2, len(nums)): # 前面的两个数字保留
            if nums[i]!=nums[stack_size-2]: # 和栈顶下方的元素做比较
                nums[stack_size]=nums[i] # 入栈
                stack_size+=1
        return min(stack_size, len(nums)) 