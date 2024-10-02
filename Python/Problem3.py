#Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        start = 0
        res = 0
        for i in range(len(s)):
            while s[i] in current:
                current.remove(s[start])
                start += 1
            current.add(s[i])
            res = max(res, i - start + 1)

        return res