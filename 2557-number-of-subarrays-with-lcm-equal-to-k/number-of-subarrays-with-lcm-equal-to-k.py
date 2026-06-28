class Solution(object):
    def gcd(self,a,b):
        if a==0:
            return b
        return self.gcd(b%a,a)
    def subarrayLCM(self, nums, k):
        c=0
        for i in range(0,len(nums)):
            lcm=1
            for j in range(i,len(nums)):
                lcm=(lcm*nums[j])//self.gcd(lcm,nums[j])
                if lcm==k:
                    c+=1
                elif lcm>k:
                    break
        return c

        
        