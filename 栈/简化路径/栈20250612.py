# 题意：给定一组由/隔开的字符串（忽略空串和.），从左到右遍历这些字符串，依次删除每个..及其左侧的字符串（模拟返回上一级目录）

# 思路：
# 1. 将path按照/分割，得到一个字符串列表
# 2. 遍历字符串列表的同时，用栈维护遍历过的字符串
# （1）如果当前字符串是空串或者是.，则跳过
# （2）如果当前字符串不是..，则将字符串入栈
# （3）遇到的字符串是..，弹出栈顶元素，模拟返回上一级目录

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths=path.split('/')
        st=[] # 栈
        for item in paths:
            if item=='' or item=='.': # 如果当前字符是空串或者是.，则跳过
                continue
            if item!='..': # 如果当前字符串不是..，则将字符串入栈
                st.append(item)
            elif st: # 遇到的字符串是..，则弹出栈顶元素
                st.pop()
        return '/'+'/'.join(st)