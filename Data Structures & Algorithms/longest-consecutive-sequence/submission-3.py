from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        existing=set()
        for i in nums:
            existing.add(i)
     
        max_count=0
        for i in nums:
            count=1
            if i-1 not in existing:
                j=i
                while j+1 in existing:
                    j+=1
                    count+=1
            max_count=max(max_count,count)
        return max_count

        
        