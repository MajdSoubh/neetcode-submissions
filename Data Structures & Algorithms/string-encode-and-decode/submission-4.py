class Solution:

    def __init__(self):
        self.separator = "-----"
        self.empty = "*****"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.empty
        return self.separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.empty:
            return []
        st = 0
        end = s.find(self.separator)
        result = []
        while (end != -1):
            result.append(s[st:end])
            st = end + len(self.separator)
            end = s.find(self.separator, end+len(self.separator))
        result.append(s[st:])
        return result