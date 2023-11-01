#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        I'm thinking, to check for paraenthesis, I'll still need to go through
        the whole collection of characters in s.
        Then, I can technically go through all the characters in s and store 
        all the paraenthesis in a different list (or set even).
        At the end, we do a check if the paranthesis were inputted correctly.
        
        I'm thinking we have a list of the opening parentheses, and have
        something that directs it to the closing
        
        then when the closing is found, we delete it from the list
        
        make sure that this list is a stacking list so that the last to enter
        is the first to exit (to make sure the brackets are closed properly)
        
        '''
        
        parentheses ={
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif len(stack) == 0 or char != parentheses[stack.pop()]:
                return False
            
        return len(stack) == 0
        
# @lc code=end

