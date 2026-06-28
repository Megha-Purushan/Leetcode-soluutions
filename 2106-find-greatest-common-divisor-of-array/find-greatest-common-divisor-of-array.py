class Solution(object):
    def findGCD(self, nums):
        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
        a=min(nums)
        b=max(nums)
        return gcd(a,b)
        
        