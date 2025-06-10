# 思路：本题等同于定长滑窗，也就是判断nums中是否存在一个长为min(k+1, n)的连续子数组，包含相同元素
# 核心思路：维护一个长为min(k+1, n)的滑动窗口，用hash集合维护这个窗口内的元素。在元素x进入窗口之前，判断该元素是否在窗口内存在，如果存在的话，说明x加入窗口之后，窗口内有重复元素
# 步骤：
# 1. 创建一个空的哈希集合
# 2. 遍历nums
# 3. 判断x=nums[i]是否在哈希集合中，如果在则返回True
# 4. 如果不在，则将x加入到哈希集合中
# 5. 如果i>=k，那么下一轮循环nums[i-k]不在窗口中，将其移出哈希集合

# 时间复杂度：O(n)
# 空间复杂度：O(min(k, n))
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set=set()
        for i, x in enumerate(nums):
            if x in hash_set:
                return True
            hash_set.add(x)
            if i>=k: # 判断定长窗口的长度是否超过了k，如果超过的话则移出左边的元素
                hash_set.remove(nums[i-k])
        return False

        