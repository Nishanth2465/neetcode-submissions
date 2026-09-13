class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=99999999
        cprof=0
        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]
            cprof=max(prices[i]-low,cprof)
        return cprof

        