class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        more=max(candies)
        result=[]
        for i in candies:
            if i + extraCandies >=more:
                result.append(True)
            else:
                result.append(False)
        return result

        