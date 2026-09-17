class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        answer=high
        
        while high>=low:
            current_best=0
            mid=int((high+low)/2)
            for i in piles:
                current_best+=-(-i//mid)
            if current_best<=h:
                answer=(min(answer,mid))
                high=mid-1
            else:
                low=mid+1
                
        return answer