import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for v in itertools.permutations(nums):
            print(v)
            ans.append(v)
        return ans