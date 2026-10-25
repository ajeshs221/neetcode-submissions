class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ar=[]
        for i in range(0,len(nums)):
            if nums[i] in ar:
                return True
            else:
                ar.append(nums[i]) 
        return False
    
        