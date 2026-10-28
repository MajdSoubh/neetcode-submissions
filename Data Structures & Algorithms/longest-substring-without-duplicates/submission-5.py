class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        result = 0
        for i, c in enumerate(s):
            if c in seen:
                while c in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(c)
            result = max(result, len(seen))
        return result