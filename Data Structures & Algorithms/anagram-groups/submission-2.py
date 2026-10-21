
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [("".join(sorted(str)), str) for str in strs]
        strs = sorted(strs, key=lambda item: item[0])
        str_lens = {}
        for str in strs:
            if len(str[0]) not in str_lens:
                str_lens[len(str[0])] = [str]
            else:
                str_lens[len(str[0])] = [*str_lens[len(str[0])], str]

        result = []
        for str_list in str_lens:
            str_list = str_lens[str_list]
            prev = ""
            similar_str = []
            for str in str_list:
                if str[0] == prev:
                    similar_str.append(str[1])
                else:
                    if len(similar_str) != 0:
                        result.append([*similar_str])
                        similar_str.clear()
                    similar_str.append(str[1])
                    prev = str[0]
            if len(similar_str) != 0:
                result.append([*similar_str])

        return result