# 题意：在0, 1, 2, ..., 2n-1中选出n个数，填入左括号，其余n位置填入右括号
# 暴力法：生成2**(2n)个由括号字符构成的序列，然后我们检查每一个是否有效即可
# 时间复杂度：O(2**2n *n) 对于2**2n个序列中的每一个，用于建立和验证该序列的复杂度为O(n)
# 空间复杂度：O(n) 需要的空间取决于递归的栈的深度，每一层递归函数需要O(1)的空间，最多递归2n层
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            if len(A)==2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()

                A.append(')')
                generate(A)
                A.pop()
        
        def valid(A):
            """类似用栈判断括号是否有效"""
            bal=0
            for c in A:
                if c=='(':
                    bal+=1
                else:
                    bal-=1
                if bal<0:
                    return False
            return True if bal==0 else False

        ans = []
        generate([])
        return ans
        