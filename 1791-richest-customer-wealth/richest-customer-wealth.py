class Solution(object):
    def maximumWealth(self, accounts):
        richest=0
        for i in accounts:
            wealth=sum(i)
            if wealth>richest:
                richest=wealth
        return richest
        
        
        