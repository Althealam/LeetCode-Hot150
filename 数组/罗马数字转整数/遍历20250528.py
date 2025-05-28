# 思路：
# 1. 输入的字符串满足小的数字在大的数字的右边，则将每个数字都看作是一个单独的值，累加每个字符对应的数值即可
# 2. 输入的字符串存在小的数字在大的数字的左边，需要根据规则去减去小数字，可以把该数字的符号取反
# 使用一个ans计算遍历的过程中每个字符的值
class Solution:
    def romanToInt(self, s: str) -> int:
        map={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans=0
        for i, ch in enumerate(s):
            value=map[ch]
            if i<len(s)-1 and value<map[s[i+1]]: # 小的数字在大的数字的左边
                ans-=value
            else:
                ans+=value # 小的数字在大的数字的右边
        return ans
        