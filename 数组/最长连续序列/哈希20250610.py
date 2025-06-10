# 核心思路：对于nums中的元素x，以x为起点，不断查找下一个数x+1, x+2是否在nums中，并统计序列的长度
# 注意：
# 1. 将nums中的元素都放到一个哈希集合中，这样可以O(1)判断数字是否在nums中（如果是1 1 2 3 4的话1会重复计数）
# 2. 如果x-1在哈希集合汇总，则不以x为起点

# 时间复杂度：O(n)，其中n是nums的长度
# 空间复杂度：O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0 # 统计最长连续序列的长度
        st=set(nums) # 把nums转换为hash集合
        for x in st: # 遍历哈希集合
            if x-1 in st: # 如果x-1在集合中，则不以x为起点（因为以x-1为起点的序列长度一定比以x为起点的序列要长）
                continue
            # 循环遍历，判断y是否在哈希集合中
            # x是序列的起点
            y = x+1
            while y in st: # 不断查找下一个数是否在哈希集合中
                y+=1
            # 循环结束后，y-1是最后一个在哈希集合中的数
            ans=max(ans, y-x) # 从x到y-1总共有y-x个数
        return ans