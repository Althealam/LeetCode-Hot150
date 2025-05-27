# 分析：answer[i]等于nums中除了nums[i]之外其余各个元素的乘积
# 如果知道了i左边所有数的乘积，以及i右边所有数的乘积，就可以得到answer[i]
# 1. 定义pre[i]表示从nums[0]到nums[i-1]的乘积：pre[i]=pre[i-1]*nums[i-1]
# 2. 定义suf[i]表示从nums[i+1]到nums[n-1]的乘积：suf[i]=suf[i+1]*nums[i+1]
# 初始值：pre[0]=suf[n-1]=1 这两个表示空子数组的元素乘积

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # 求出pre数组，也就是nums[0]到nums[i-1]的数组的乘积
        pre=[1]*len(nums)
        for i in range(1, n):
            pre[i]=pre[i-1]*nums[i-1]
        
        # 求出sub数组，也就是nums[n-1]到nums[i]的数组的乘积
        sub=[1]*len(nums)
        for i in range(n-2, -1, -1): 
            sub[i]=sub[i+1]*nums[i+1]
        
        return [p*s for p, s in zip(pre, sub)]
            