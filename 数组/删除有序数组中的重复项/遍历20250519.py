# 思路：定义k作为唯一数组的下标 每次遍历的时候都判断当前元素与前一个元素是否相等，如果相等的话则不加入该元素，不相等的话则加入该元素
# 1. 初始化k=1，表示保留的元素要填入的下标
# 2. 从i=1开始遍历nums
# 3. 如果nums[i]==nums[i-1]，那么nums[i]是重复项，不保留
# 如果nums[i]!=nums[i-1]，那么nums[i]不是重复项，保留

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k