# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            if target-num in hashmap: # 判断target-num是否在hashmap中
                return [hashmap[target-num], i] # 如果在的话则直接返回
            hashmap[num]=i # 不在的话则填充hashmap
        return None