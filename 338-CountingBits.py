class Solution:
    def countBits(self, n: int) -> List[int]:
        def digit_sum(n):
            # 各桁の和を求める
            # 計算量: O(logN)
            ans = 0
            while n > 0:
                ans += n % 10
                n //= 10
            return ans
        ans = []
        for i in range(n+1):
            ans.append(digit_sum(int(bin(i)[2:])))
        return ans