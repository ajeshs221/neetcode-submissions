class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashs={}
        current_length=0
        max_length=0
        start=0
        for i in range(0,len(s)):
            if s[i] in hashs and hashs[s[i]] >= start:
                start=hashs[s[i]]+1
            hashs[s[i]]=i
            current_length=i-start+1
            if current_length > max_length:
                max_length=current_length
        return max_length