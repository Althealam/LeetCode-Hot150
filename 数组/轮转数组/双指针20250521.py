# 思路：
# 轮转k个元素：1.反转整个数组 2. 反转前k个元素 3. 反转后n-k个元素

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left<right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
        n=len(nums)
        k=k%n # 轮转k次相当于轮转k%n次
        reverse(0, n-1) # step1：反转整个数组
        reverse(0, k-1) # step2：反转前面k个元素
        reverse(k, n-1) # step3：反转后n-k个元素
        
        