# 思路：单调栈
# 栈中存储还没找到右边第一个超过其元素值的元素，最后要返回的峰值就是这个栈内的元素
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        st = []
        for i in range(len(nums)):
            if len(st)==0:
                st.append(i)
            else:
                if nums[i]>nums[st[-1]]:
                    st.pop() # 弹出栈顶元素，栈顶元素找到了右边第一个超过其元素值的元素
                    st.append(i)
        return st[0]
        