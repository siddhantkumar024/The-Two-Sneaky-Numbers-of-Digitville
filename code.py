class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        f=[]
        for i in range(1,n+1):
            if i<n and nums[i-1]==nums[i]:
                f.append(nums[i-1])
        return f
        
