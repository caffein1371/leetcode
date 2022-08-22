class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            #print(bin(i)[2:])
            #print(sum(list(map(int, str(bin(i)[2:])))))
            ans.append(sum(list(map(int, str(bin(i)[2:])))))
        return ans
        