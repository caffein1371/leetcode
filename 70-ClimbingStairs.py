class Solution:
    def climbStairs(self, n: int) -> int:
        #0, 1, 1, 2, 3, 5, 8, 13, 21
        a=0
        b=1
        for i in range(n):
            #a, b = b, a+b
            temp = b
            b = a + temp
            a = temp
        
        return b
            