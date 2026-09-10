from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)
        for i in strs:
            ar=[0]*26
            for j in i:
                ar[ord(j)-ord("a")]+=1
                
                
            d[tuple(ar)].append(i)
        return list(d.values())
                
            
        