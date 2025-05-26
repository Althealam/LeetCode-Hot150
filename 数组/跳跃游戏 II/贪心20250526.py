# 思路：贪心法，每次都尽量多跳一些，就可以让总的步数最少
class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt=0 # 跳跃的总步数
        cur_right=0 # 目前能够跳到的最远距离
        next_right=0 # 下一次能够跳到的最远距离
        for i in range(len(nums)-1):
            next_right=max(i+nums[i], next_right)
            if i==cur_right:  # 到达了目前可以跳到的最远边界
                cur_right=next_right
                cnt+=1
        return cnt
