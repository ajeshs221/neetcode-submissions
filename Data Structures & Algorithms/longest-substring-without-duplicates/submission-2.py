class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashs={}
        start=0
        current_longest=0
        longest=0
        for i in range(0,len(s)):
            if s[i] in hashs and hashs[s[i]] >= start:
                start=hashs[s[i]]+1
            hashs[s[i]]=i
            current_longest=i-start+1
            if current_longest > longest:
                longest=current_longest
        print(longest)
        return longest
        