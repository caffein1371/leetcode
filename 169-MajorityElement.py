class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans= list(set(nums))
        for i in range(len(ans)):
            if nums.count(ans[i])>=len(nums)/2:
                return ans[i]