class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        st = 0
        while (st != len(s)):
            end = s.find('#', st)
            size = int(s[st:end])
            sub_str = s[end+1:end+1+size]
            result.append(sub_str)
            st = end+1+size
        return result
