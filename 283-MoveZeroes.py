class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)+1):
            if nums[-i]==0:
                nums.pop(-i)
                nums.append(0)

        return nums           