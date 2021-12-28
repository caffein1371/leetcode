class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        orinum = len(nums)
        nums= set(sorted(nums))
        ans = []
        for i in range(1,orinum+1):
            if i not in nums:
                ans.append(i)
        return ans