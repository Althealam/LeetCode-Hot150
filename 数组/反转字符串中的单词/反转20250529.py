class Solution:
    def reverseWords(self, s: str) -> str:
        list_s=s.split(" ")
        res=[]
        for item in list_s:
            if item!="":
                res.append(item)
        return " ".join(res[::-1])