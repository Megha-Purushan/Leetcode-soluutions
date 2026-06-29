class Solution(object):
    def countPrimes(self, n):
        c=0
        prime=[True]*(n)
        
        for i in range(2,n):
            if prime[i]:
                j=i*i
                while j<n:
                    prime[j]=False
                    j=j+i
        for i in range(2,n):
            if prime[i]:
                c+=1
        return c

            
        
        