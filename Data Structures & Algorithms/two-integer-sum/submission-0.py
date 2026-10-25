class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh={}
        for i,n in enumerate(nums):
            comp=target-n
            if comp in hashh:
                return [hashh[comp], i]
            else:
                hashh[n]=i

        