
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        result=[]
        arr=[[] for i in range(len(nums)+1)]
        for i,j in count.items():
            arr[j].append(i)

        for i in range(len(nums),0,-1):
            for j in arr[i]:
                result.append(j)
                if len(result)==k:
                    return result
                
        