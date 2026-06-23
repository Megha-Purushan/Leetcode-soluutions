class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=""
        for i in zip(*strs):
            s=set(i)
            if len(s)==1:
                prefix=prefix+i[0]
            else:
                break
        return prefix

        
        