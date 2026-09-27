class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums=set()
        temp=set()
        sums.add(0)
        target=sum(nums)/2
        for i in range(len(nums)):
            temp=set()
            for j in sums:
                temp.add(j+nums[i])
                temp.add(j)
            sums=temp
            
        return target in sums
