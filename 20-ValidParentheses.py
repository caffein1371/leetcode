class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)-1):
            print (s[i])
            #print (s[i+1::])
            ans = False
            if s[i]=="(" and (s[i+1]!="]" or s[i+1]!="}") and ")" in s[i+1::]:
                print (1)
                ans = True
            elif s[i]=="[" and (s[i+1]!=")" or s[i+1]!="}") and "]" in s[i+1::]:
                print (2)
                ans = True
            elif s[i]=="{" and (s[i+1]!=")" or s[i+1]!="]") and "}" in s[i+1::]:
                print (3)
                ans = True
            if s[i]=="(" and (s[i+1]=="]" or s[i+1]=="}"):
                print (4)
                ans = False
            elif s[i]=="[" and (s[i+1]==")" or s[i+1]=="}"):
                print (5)
                ans = False
            elif s[i]=="{" and (s[i+1]=="]" or s[i+1]==")"):
                print (6)
                ans = False
                
        return ans
                
            