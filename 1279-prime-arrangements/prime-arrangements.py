class Solution(object):
    def numPrimeArrangements(self, n):
        c=0
        prime=[True]*(n+1)

        for i in range(2,n+1):
            if prime[i]:
                j=i*i
                while j<=n:
                    prime[j]=False
                    j=j+i
        for i in range(2,n+1):
            if prime[i]:
                c=c+1
        MOD = 10**9 + 7
        def fact(n):
            fact=1
            for i in range(2,n+1):
                fact=(fact*i)%MOD
            return fact
        return (fact(n-c)*fact(c))%MOD


        