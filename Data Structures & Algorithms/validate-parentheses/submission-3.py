class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        diction = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        i = 0
        while i in range(len(s)):
            if s[i] in ["(","{","["]:
                stack.append(s[i])
                # print(stack)
                i +=1
            else:
                # print(s[i])
                # print(diction[stack.pop()])
                try:
                    if s[i] == diction[stack.pop()]:
                        # print(stack)
                        i += 1
                        continue
                    else:
                        return False
                except IndexError:
                    return False
        if stack:
            return False
        return True