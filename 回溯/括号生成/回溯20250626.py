# 题意：在0, 1, 2, ..., 2n-1中选出n个数，填入左括号，其余n位置填入右括号
# 改进方法：在序列仍然保持有效的时候才添加(或者)，而不是像暴力法一样每次都添加括号
# 时间复杂度：O(4**n/n**(1/2))
# 空间复杂度：O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S)==2*n:
                ans.append(''.join(S))
                return 
            if left<n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right<left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()
        backtrack([], 0, 0)
        return ans