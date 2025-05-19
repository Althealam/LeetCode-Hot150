# 思路：相同的元素必然连续。遍历数组，检查每个元素是否应该被保留，如果应该被保留则将其移动到指定位置
# 定义slow和fast分别为慢指针和快指针，其中慢指针表示处理好的数组的长度，快指针表示已经检查过的数组的长度
# 注意：由于我们要保证相同元素最多出现两次，因此我们检查nums[slow-2]和nums[fast]是否相同，如果相同的话则说明nums[fast]已经出现了两次了，如果不相同的话则nums[fast]最多出现过一次

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 2, 2
        while fast<len(nums):
            if nums[slow-2]!=nums[fast]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow
