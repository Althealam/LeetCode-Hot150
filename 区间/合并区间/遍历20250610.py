# 使用idx遍历nums中的索引，记录cur_num
# 判断cur_num+1是否在nums中，如果不在的话，则在ans中加入答案值
# 如果在的话，则不断的寻找右边界，直到右边的元素不存在为止
# 时间复杂度：O(n)
# 空间复杂度：O(n)


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        idx=0
        while idx<len(nums):
            cur_num=nums[idx]
            if cur_num+1 not in nums:
                ans.append(f"{cur_num}")
                idx+=1
            else:
                left=cur_num
                next_num=cur_num+1
                while next_num in nums:
                    right=next_num
                    next_num+=1
                    idx+=1
                ans.append(f"{left}->{right}")
                idx+=1
        return ans
                

                
        