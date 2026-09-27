class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            right=i
            left=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                right+=1
                left-=1
        for i in range(len(s)):
            right=i+1
            left=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                right+=1
                left-=1
        return count

                
                

            
        