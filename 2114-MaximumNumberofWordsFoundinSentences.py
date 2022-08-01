class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            temp=s.split()
            ans = len(temp) if ans<len(temp) else ans
        return ans