class Solution:
    def trap(self, height: List[int]) -> int:
        a=list()
        water=0
        final=0
        i=0
        j=0
        final2=0
        cur_height=0
        while i<len(height):
            if height[i]>=cur_height:
                cur_height=height[i]
                final=water
                j=i
            water+=cur_height-height[i]
            i+=1

        cur_height=0
        water=0
        start=len(height)-1
        while start>=j:
            if height[start]>cur_height:
                cur_height=height[start]
                final2=water
            water+=cur_height-height[start]
            start-=1
        return final+final2

            
            
            
            

            
            
        