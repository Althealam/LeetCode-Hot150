# 时间复杂度：O(1)
# 空间复杂度：O(1)
class RandomizedSet:

    def __init__(self):
        """初始化RandomizedSet对象"""
        self.nums=[]
        self.indices={}
        

    def insert(self, val: int) -> bool:
        """当val不存在时，向集合中插入该项并返回True"""
        if val in self.indices:
            return False
        self.indices[val]=len(self.nums)
        self.nums.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        """当val存在时，从集合中移除该项并返回True"""
        if val not in self.indices:
            return False
        id=self.indices[val]
        self.nums[id]=self.nums[-1]
        self.indices[self.nums[id]]=id
        self.nums.pop()
        del self.indices[val]
        return True
        

    def getRandom(self) -> int:
        """随机返回现有集合中的一项"""
        return choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()