class Solution:
    def numberOfSteps(self, num: int) -> int:
        self.ans = 0
        def divide(num):
            if num==0:
                return self.ans
            if num%2==0 and num!=0:
                self.ans+=1
                return divide(num/2)
            elif num%2==1:
                self.ans+=1
                return divide(num-1)
        return divide(num)