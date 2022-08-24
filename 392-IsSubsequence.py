class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s)==0:
            return True
        for i in range(len(t)):
            print (t)
            print (s)
            if t[i] in s and len(s)!=0:
                s.remove(t[i])
            if len(s)==0:
                return True
            
        if len(s)!=0:
            return False