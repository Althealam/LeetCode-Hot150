class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=s.split(" ")
        ans=[]
        for r in res:
            if r!="":
                ans.append(r)
        return len(ans[-1])
        