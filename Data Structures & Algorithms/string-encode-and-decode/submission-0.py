
class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for word in strs:
            sol += str(len(word)) + "#" + word
        print(sol)
        return sol

    def decode(self, s: str) -> List[str]:
        i = 0
        sol = []
        while i < len(s):
            temp_num = ""
            while s[i] != "#":
                temp_num += s[i]
                i+=1
            i+=1#move onto the char
            temp_num = int(temp_num)
            sol.append(s[i:temp_num+i])
            i = temp_num+i
        return sol





            
