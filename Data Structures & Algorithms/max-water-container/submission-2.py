class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1

        max_water=0
        while i<j:
            water=min(heights[i],heights[j])*(j-i)
            if water>max_water:
                max_water=water
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water
        

            
            



        