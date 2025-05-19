# 思路：考虑到不能覆盖nums1原来的元素，因此考虑使用逆向双指针
# 定义指针分别指向nums1[m-1]和nums2[n-1]，将较大的值放到nums1的末尾，设置指针分别为p0和p1，设置tail=m+n-1（表示目前正在遍历的nums1数组下标）
# 遍历nums1，判断nums1[p0]和nums2[p1]
# （1）nums1[p0]>nums2[p1]: nums1[tail]=nums1[p0]
# （2）nums1[p0]<nums2[p1]: nums1[tail]=nums2[p1]
# （3）nums1[p0]==nums2[p1]: nums1[tail]=nums1[p0]

# 时间复杂度：O(m+n)，nums1和nums2中的每个元素最多被遍历一次
# 空间复杂度：O(m+n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        tail = m+n-1
        while p1>=0 or p2>=0:
            if p1==-1:
                nums1[tail]=nums2[p2]
                p2-=1
            elif p2==-1:
                nums1[tail]=nums1[p1]
                p1-=1
            elif nums1[p1]>nums2[p2]:
                nums1[tail]=nums1[p1]
                p1-=1
            else:
                nums1[tail]=nums2[p2]
                p2-=1
            tail-=1