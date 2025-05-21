
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map=defaultdict(int)
        for num in nums:
            if num not in hash_map.keys():
                hash_map[num]=1
            else:
                hash_map[num]+=1
            if hash_map[num]>len(nums)//2:
                return num
