class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    #print ("[{0},{1}]".format(i,j))
                    ans.append(i)
                    ans.append(j)
                    return ans