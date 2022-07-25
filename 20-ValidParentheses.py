class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dict ={")":"(","}":"{","]":"["}
        for i in s:
            #if i is ( or[ , { ,pushes to stack.
            if i in dict.values():
                stack.append(i)
            #if i is　) or ] , },checks the stack whether ( or {,[.
            elif i in dict.keys():
                if stack==[] or dict[i]!=stack.pop():
                    return False
        # if stack is empty,returns True
        if stack==[]:
            return True