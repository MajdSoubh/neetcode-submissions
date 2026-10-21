class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first =dict()
        second = dict()
        if len(s) != len(t):
             return False
        for c in s:
            if c not in first:
                first[c] = 1
            else:
                first[c]= first[c] + 1

        for c in t:
                if c not in second:
                    second[c] = 1
                else:
                    second[c]= second[c] + 1
        for c in s:
             if c not in first or c not in second or first[c] != second[c]:
             
                  return False

        return True
                        