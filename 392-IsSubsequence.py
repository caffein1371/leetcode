class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        for i in range(len(t)):
            print (t[i])
            if t[i] in s and len(s)!=0:
                s=s.removeprefix(t[i])
            print (s)
            if len(s)==0:
                return True
        if len(s)!=0:
                return False
                    