class Solution(object):
    def primePalindrome(self, n):
        def isprime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        def ispalindrome(x):
            s = str(x)
            return s == s[::-1]

        while True:
            if ispalindrome(n) and isprime(n):
                return n
            n += 1
            # Optimization: skip even-length palindromes > 11
            if 10**7 < n < 10**8:
                n = 10**8


            
        