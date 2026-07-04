class Solution(object):
    def addBinary(self, a, b):
        c=int(a,2)
        d=int(b,2)
        s=c+d
        return bin(s)[2:]
        