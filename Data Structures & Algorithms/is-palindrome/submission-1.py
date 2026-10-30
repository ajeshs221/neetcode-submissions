class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=s.lower()
        start=0
        end=len(ss)-1
        while start < end:
            while start<end and not ss[start].isalnum():
                start+=1
            while start<end and not ss[end].isalnum():
                end-=1
            if ss[start]!=ss[end]:
                return False
            start+=1
            end-=1
        return True