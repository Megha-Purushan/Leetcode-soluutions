class Solution(object):
    def thirdMax(self, nums):
        n=list(set(nums))
        n.sort()
        if len(n)>=3:
            return n[-3]
        else:
            return max(n)

    

        