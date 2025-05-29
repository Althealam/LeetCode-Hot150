# 思路：按照顺序遍历字符串s的时候，每个字符c在N字形中对应的行索引先从s1增大到sn，再从sn减小到s1，因此可以定义一个diff表示i为递增的还是递减的
# 思路：
# 1. 定义matrix存储每一行的数据
# 2. i=1表示将元素插入到matrix的第i行，diff=1表示i是递增的，diff=-1表示i是递减的
# 3. 遍历更新matrix，每次都用i加上diff的值，表示向上迭代遍历一行，或者是向下迭代遍历一行
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix=[[] for _ in range(len(s))]
        
        # diff==-1表示i递减，diff==1表示i递增
        i=1
        diff=-1

        # 遍历更新matrix
        for char in s:
            i+=diff
            if i==0 or i==numRows-1:
                diff*=-1 # 变更递增或者递减
            matrix[i].append(char)
        
        # 拼接
        # return matrix
        return ''.join(''.join(row) for row in matrix)


        