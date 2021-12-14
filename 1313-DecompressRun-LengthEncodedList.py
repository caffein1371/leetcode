class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in range(len(nums)):
            if i%2==1:
                ans+= [nums[i]]*nums[i-1]
        return ans