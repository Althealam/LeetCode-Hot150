# 思路：遇到左括号则入栈其对应的右括号，遇到右括号则弹出栈顶元素
# 三种不匹配的情况
# 1. 字符串里左括号多余，因此不匹配
# 2. 字符串里右括号多余，因此不匹配
# 3. 字符串里括号没有多余，但是括号的类型没有匹配上，因此不匹配

# 判断方法：
# 1. 已经遍历完所有字符串，但是栈不为空，因此有左括号没找到匹配的右括号
# 2. 遍历字符串的过程中，发现栈里没有要匹配的字符
# 3. 遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明有右括号没有找到匹配的左括号
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch=='(':
                st.append(')')
            elif ch=='[':
                st.append(']')
            elif ch=='{':
                st.append('}')
            elif not st or st[-1]!=ch: # 栈为空（没有匹配的字符），或者当前的栈顶元素不匹配
                return False
            else:
                st.pop() # 遇到了符合的元素
        return True if not st else False # 栈为空了则为True，栈不为空说明还有左括号没有匹配上
