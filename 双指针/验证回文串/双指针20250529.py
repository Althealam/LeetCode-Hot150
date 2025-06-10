# 思路：
# 1. 初始化左右指针i=0, j=n-1
# （1）如果s[i]既不是字母也不是数字，右移左指针，i+=1
# （2）如果s[j]既不是字母也不是数字，左移右指针，j-=1
# （3）否则，如果s[i]和s[j]转换为小写后相等，则i+=1 j-=1
# （4）否则，不是回文串

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if not s[i].isalpha() and not s[i].isdigit():
                i+=1
            elif not s[j].isalpha() and not s[j].isdigit():
                j-=1
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
