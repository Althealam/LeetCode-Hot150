# 思路：
# 1. 用hash构建s->t和t->s的映射字典
# 2. 判断一下一个元素是否有对应多个映射，如果是的话则范围False

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t={}
        t_to_s={}
        for i in range(len(s)):
            if s[i] not in s_to_t: # 构建s到t的映射
                s_to_t[s[i]]=t[i]
            else: # 如果s[i]已经在映射集合中了，则判断是否是唯一映射
                if s_to_t[s[i]]!=t[i]:
                    return False
            if t[i] not in t_to_s: # 构建t到s的映射
                t_to_s[t[i]]=s[i]
            else: # 如果t[i]已经在映射集合中了，则判断是否是唯一映射
                if t_to_s[t[i]]!=s[i]:
                    return False
        return True
                
        