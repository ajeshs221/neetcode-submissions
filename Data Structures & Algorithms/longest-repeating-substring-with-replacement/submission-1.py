class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map={}
        result=0
        left=0
        right=0
        for right in range(0,len(s)):
            count_map[s[right]]= 1 + count_map.get(s[right],0)
            while (right-left+1) - max(count_map.values()) > k:
                count_map[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
        print (result)
        return result