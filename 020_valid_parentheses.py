class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        push_set = ['(', '{', '[']
        poll_set = [')', '}', ']']
        dic = {')':'(', '}':'{', ']':'['}
        
        for s1 in s:
            if s1 in push_set:
                stack.append(s1)
            elif s1 in poll_set:
                if not stack or dic[s1] != stack.pop():
                    return False
            else:
                return False
        if stack:
            return False
        return True

'''
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
'''