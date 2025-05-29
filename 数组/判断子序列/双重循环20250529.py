# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 判断s是否是t的子串
        # 如果s为空串，则直接返回True
        if not s:
            return True
        
        i=0 # 遍历s的位置
        # 遍历t的字符c，判断是否与s[i]匹配，如果匹配的话则i+=1
        for c in t:
            if s[i]==c:
                i+=1 # 开始判断s的下一个字符
                if i==len(s): # 已经遍历完s了
                    return True 
        return False
        