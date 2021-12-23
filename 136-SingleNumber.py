import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp =[k for k, v in collections.Counter(nums).items() if v == 1]
        return temp[0]