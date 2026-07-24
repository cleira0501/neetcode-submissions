class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        out = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in str_dict:
                out[str_dict[sorted_word]].append(word)
            else:
                str_dict[sorted_word] = len(out)
                out.append([word])
        return out
