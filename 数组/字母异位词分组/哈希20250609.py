# 时间复杂度：O(nmlogm)，其中n为strs的长度，m是strs[i]的长度。每个字符串排序需要O(mlogm)的时间，我们有n个字符串，因此总共为O(mnlogm)
# 空间复杂度：O(mn)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list) # 构建hash，key是经过排序后的元素，value是排序后相对应的元素值
        for s in strs:
            sorted_s=''.join(sorted(s)) # 对s进行排序
            d[sorted_s].append(s) # 如果其排序后相同，则加入
        return list(d.values())
        