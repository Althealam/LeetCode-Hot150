# 思路：定义双指针left和right，其中left表示的是无重复字符的子串的开始位置，right表示的是无重复字符的子串的结束位置
# 用一个字典来计算每个元素的出现次数
# 如果窗口内有重复元素，则右移left，然后将left的元素的次数减去1，更新ans的值，不停的移动left直到窗口内没有重复元素

# 时间复杂度：O(n)，其中n为s的长度（left至多增加n次，所以整个二重循环至多循环O(n)次）
# 空间复杂度：O(1)，本来应该是O(m)，然后m是字符集合的大小，但是因为m<=128，因此为O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0 # 无重复字符的子串的最小长度
        left=0 # 无重复字符的子串的开始位置
        cnt=defaultdict(int) # 维护从left到right中各个元素的出现次数
        for right, ch in enumerate(s):
            cnt[ch]+=1 # 更新ch的出现次数
            while cnt[ch]>1: # 窗口内有重复元素
                cnt[s[left]]-=1 # left减去一个元素
                left+=1 # 缩小窗口
            ans=max(ans, right-left+1)
        return ans
        