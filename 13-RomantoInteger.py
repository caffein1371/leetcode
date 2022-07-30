class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in range(len(s)):
            ans += mydict[s[i]]
            try:
                if s[i]=="I" and s[i+1]=="V":
                    ans-=2
                elif s[i]=="I" and s[i+1]=="X":
                    ans-=2
                elif s[i]=="X" and s[i+1]=="L":
                    ans-=20
                elif s[i]=="X" and s[i+1]=="C":
                    ans-=20
                elif s[i]=="C" and s[i+1]=="D":
                    ans-=200
                elif s[i]=="C" and s[i+1]=="M":
                    ans-=200
            except:
                pass
            print (ans)
        return ans