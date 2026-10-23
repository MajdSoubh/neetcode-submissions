class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        for c in s:
            if not c.isalnum():
                s = s.replace(c, "")

        s = s.lower()
        if s == s[::-1]:
            return True
        return False