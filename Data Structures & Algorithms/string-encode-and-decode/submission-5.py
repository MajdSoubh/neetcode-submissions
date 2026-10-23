class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        st = 0
        end = 0
        sizes = []
        while (s[st] != '#'):
            end = s.find(',', st)
            size = int(s[st:end])
            sizes.append(size)
            st = end+1

        starting_str_ind = s.find('#')+1
        s = s[starting_str_ind:]
        st = 0
        for size in sizes:
            sub_result = s[st:st+size]
            result.append(sub_result)
            st += size

        return result