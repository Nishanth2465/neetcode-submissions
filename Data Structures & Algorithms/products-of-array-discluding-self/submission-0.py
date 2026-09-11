class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[]
        pre = [1] * (n + 1)    
        suf = [1] * (n + 1)     

        for i in range(n):
            pre[i+1] = pre[i] * nums[i]

        for i in range(n-1, -1, -1):
            suf[i] = suf[i+1] * nums[i]

        for i in range(n):
            ans.append(pre[i] * suf[i+1])    

        return ans