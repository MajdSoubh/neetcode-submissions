
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_count = {}
        for str in strs:
            sstr = "".join(sorted(str))
            if sstr not in str_count:
                str_count[sstr] = [str]
            else:
                str_count[sstr] = [*str_count[sstr], str]

        result = []
        for str_key in str_count:
            sub_result = []
            strs = str_count[str_key]
            for str in strs:
                sub_result.append(str)
            result.append(sub_result[:])
        return result