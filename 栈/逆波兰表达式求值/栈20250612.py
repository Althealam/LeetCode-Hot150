# 思路：定义一个栈，每次遇到数字则入栈，遇到计算符号则出栈
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for item in tokens:
            if item not in {'+', '-', '*', '/'}:
                st.append(int(item))
            else:
                # 先入栈后的后出栈
                num1=st.pop() # 右边的数字
                num2=st.pop() # 左边的数字
                if item=='+':
                    st.append(int(num1)+int(num2))
                elif item=='-':
                    st.append(int(num2)-int(num1))
                elif item=='*':
                    st.append(int(num1)*int(num2))
                else:
                    st.append(int(num2)//int(num1) if int(num2)//int(num1)>0 else -(abs(num2)//abs(num1)))
        return st.pop()
        