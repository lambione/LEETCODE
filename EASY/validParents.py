# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false



def isValid(s):
        #provide a stack to see the mactching
        stack = []
        # iterate over the string to see if parents are open or not 
        for parent in s:
            # edge case, if the length of the string is odd it means some parent is not gonna be closed
            if len(s) % 2 != 0 :
                return False
            if parent == '(' or parent == '[' or parent == '{' :
                stack.append(parent)
            else :
                # if we find only closing ones then we gotta return false
                if len(stack) == 0 :
                    return False
                match = stack[-1]
                if (parent == ')' and match == '(') or (parent == ']' and match == '[') or (parent == '}' and match == '{'):
                    stack.pop()
                else :
                    return False
        # here stack must be empty 
        if len(stack) == 0:
            return True
        else:
            return False