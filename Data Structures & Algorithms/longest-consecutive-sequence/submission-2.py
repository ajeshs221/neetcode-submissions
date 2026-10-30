class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l_set=set(nums)
        start=0
        c=0
        longest=0
        for i in l_set:
            if (i-1) not in l_set:
                start=i
                c=1
            while (start+1) in l_set:
                c+=1
                start+=1
            if c > longest:
                longest=c
        #print(longest)
        return longest