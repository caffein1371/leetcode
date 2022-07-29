class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp =[]
        for i in str(x):
            #print (i)
            temp.append(i)
        temp=temp[::-1]
        x1 = ''.join(temp)
        print (x1)
        return str(x)==x1