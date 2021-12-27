class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx,mn = 0,prices[0]
        for i in range(1,len(prices)):
            #一つ前との差が大きければ＞０で、今までの値より大きければmxを更新
            if prices[i]>prices[i-1]:
                mx= max(prices[i]-mn,mx)
            else:
                mn = min(prices[i],mn)
        return mx