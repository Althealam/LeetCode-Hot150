# 思路：
# 1. 从左到右遍历strs的每一列
# 2. 假设当前遍历到第j列，从上到下遍历这一列的字母
# 3. 假设当前遍历到第i行，也就是str[i][j]。如果j等于strs[i]的长度，或者strs[i][j]!=strs[0][j]，说明这一列的字母缺失或者不全一样，那么最长公共前缀的长度为j
# 4. 如果没有中途返回，说明所有字符串都有一个等于strs[0]的前缀，那么最长公共前缀就是strs[0]

# 时间复杂度：O(nm)，其中n是strs的长度，m是strs中最短字符串的长度
# 空间复杂度：O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0] # 需要返回的答案值
        for j, c in enumerate(ans): # 遍历答案值的每一列
            for s in strs: # 遍历行，不同的字符串
                if j==len(s) or s[j]!=c: # 已经到达了当前遍历的字符串的最后一列 或者是 当前遍历的字符串的第j列不等于答案值的该列
                    return ans[:j]
        return ans
        