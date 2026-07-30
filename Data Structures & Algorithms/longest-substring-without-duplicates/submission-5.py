class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l = 0
        max_len = 0
        curr_len = 0
        seen = []
        for r in range(len(s)):
            while s[r] in seen:
                seen = seen[1:]
                curr_len -=1
                # l +=1
            
            seen.append(s[r])
            curr_len+=1
            max_len = max(max_len, curr_len)
        return max(max_len, curr_len)



           

                
            



        