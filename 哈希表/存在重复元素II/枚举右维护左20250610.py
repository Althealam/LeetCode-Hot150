# 思路：用一个hash来存储每个元素最后出现的位置
# 如果遍历到了一个元素出现在hash表中，并且该元素的位置i减去该元素上一次出现的位置小于等于k，则返回True，否则返回False

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last={}
        for i, num in enumerate(nums):
            if num in last and i-last[num]<=k:
                return True
            last[num]=i
        return False