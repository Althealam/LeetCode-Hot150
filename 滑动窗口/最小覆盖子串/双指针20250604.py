# 覆盖的定义：s的子串BACN中每个字母的出现次数都大于等于t=ABC中每个字母的出现次数
# 思路：
# 1. 定义left=-1，right=m，用来记录最短子串的左右端点，其中m是s的长度
# 2. 用一个哈希表来统计t中每个字母的出现次数
# 3. 初始化left=0，以及一个哈希表cntS，用来统计s子串中每个字母的出现次数
# 4. 遍历s，假设当前枚举的子串右端点为right，将s[right]的出现次数加1
# 5. 遍历cntS中每个字母以及出现次数，如果出现次数都大于等于cntT中的字母出现次数，更新ans的值，s[left]-=1，left+=1，重复上述步骤直到cntS有字母的出现次数小于cntT

# 时间复杂度：O(km+n)，其中k是字符集合的大小，m是s的长度，n是t的长度
# 空间复杂度：O(k)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left=-1
        ans_right=len(s)
        cnt_s=Counter() # s子串中字母的出现次数
        cnt_t=Counter(t) # t子串中字母的出现次数

        left=0
        for right, ch in enumerate(s): # 移动子串右端点
            cnt_s[ch]+=1 # 右端点字母加入子串
            while cnt_s>=cnt_t: # s涵盖t
                if right-left<ans_right-ans_left: # 找到更短的子串
                    ans_left, ans_right = left, right
                cnt_s[s[left]]-=1 # 右移left指针
                left+=1
        return '' if ans_left<0 else s[ans_left:ans_right+1]
        