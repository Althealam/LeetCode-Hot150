# 思路：
# 1. 构建哈希映射，pattern到s的映射
# 2. 和上一道题类似，判断映射是否是唯一的

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_array=s.split(" ")
        if len(s_array)!=len(pattern):
            return False
        p_to_s={}
        s_to_p={}
        for i in range(len(pattern)):
            if pattern[i] not in p_to_s:
                p_to_s[pattern[i]]=s_array[i]
            else:
                if p_to_s[pattern[i]]!=s_array[i]:
                    return False
            if s_array[i] not in s_to_p:
                s_to_p[s_array[i]]=pattern[i]
            else:
                if s_to_p[s_array[i]]!=pattern[i]:
                    return False
        return True
        