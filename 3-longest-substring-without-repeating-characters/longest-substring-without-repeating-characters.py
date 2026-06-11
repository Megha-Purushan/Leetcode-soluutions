class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        for i in range(len(s)):
            sub=""
            for j in range(i,len(s)):
                if s[j] in sub:
                    break
                sub=sub+s[j]
                length=max(length,len(sub))
        return length
      

