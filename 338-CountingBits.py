class Solution:
    def countBits(self, n: int) -> List[int]:
        temp = [bin(i).count("1") for i in range(n+1)]
        return temp