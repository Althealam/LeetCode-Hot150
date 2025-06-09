# 时间复杂度：O(n)
# 空间复杂度：O(1) 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hsh=[0]*26
        for i in range(len(s)):
            hsh[ord(s[i])-ord("a")]+=1
        for i in range(len(t)):
            hsh[ord(t[i])-ord("a")]-=1
        for i in range(26):
            if hsh[i]!=0:
                return False
        return True