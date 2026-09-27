class Solution:
    def longestPalindrome(self, s: str) -> str:
        max1=0
        max2=0
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return left+1,right-1
        for i in range(len(s)):
            a,b=expand(i,i)
            c,d=expand(i,i+1)
            if (b - a) > (max2 - max1):
                max1, max2 = a, b
            if (d - c) > (max2 - max1):
                max1, max2 = c, d
        return s[max1:max2+1]

            
        