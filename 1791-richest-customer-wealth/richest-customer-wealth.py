class Solution(object):
    def maximumWealth(self, accounts):
        rich=0
        for i in accounts:
            wealth=sum(i)
            if wealth>rich:
                rich=wealth
        return rich
        
        
        