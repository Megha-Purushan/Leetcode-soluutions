class Solution(object):
    def maxProfit(self, prices):
        minp=prices[0]
        maxp=0
        for i in prices:
            minp=min(minp,i)
            maxp=max(maxp,i-minp)
        return maxp