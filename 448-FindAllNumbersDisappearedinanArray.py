class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        temp = [i for i in range(1,len(nums)+1)]
        ans = set(nums)^set(temp)        
            
        return list(ans)