class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        maxtemp = max(nums)
        for i in range(len(nums)):
            #連続で+になる必要あるので足す
            temp+=nums[i]
            if temp >=0:
                maxtemp=max(maxtemp,temp)
            else:
                temp = 0
        return maxtemp