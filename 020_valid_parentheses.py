class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for each in s:
            if each == '(' or each == '[' or each == '{':
                stack.append(each)
            elif each == ')' and stack and stack.pop() == '(':
                continue
            elif each == ']' and stack and stack.pop() == '[':
                continue
            elif each == '}' and stack and stack.pop() == '{':
                continue
            else:
                return False
        if stack:
            return False
        return True