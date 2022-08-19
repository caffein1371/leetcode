import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common()[-1][0]