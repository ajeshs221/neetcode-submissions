class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=0
        max_water=0
        left=0
        right=len(heights)-1
        while left < right:
            water=(right-left)*min(heights[left],heights[right])
            if water > max_water:
                max_water=water
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        print(max_water)
        return max_water  