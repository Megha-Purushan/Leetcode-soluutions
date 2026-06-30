class Solution(object):
    def countBits(self, n):
        result=[]
        for i in range(0,n+1):
            b=bin(i)
            c=b.count("1")
            result.append(c)
        return result

        