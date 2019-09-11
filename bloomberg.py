"""
1. Decode string
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
"""

class Solution(object):
    def isDigit(self,xs):
        try:
            int(xs)
            return True
        except:
            return False
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[1,""]]
        num= ""
        for char in s:
            if self.isDigit(char):
                num+=char
            elif char=="[":
                stack.append([int(num),""])
                num=""
            elif char=="]":
                seq,num_ = stack.pop()
                stack[-1][1]+=seq*num_
            else:
                stack[-1][1]+=char
        return stack[0][1]

