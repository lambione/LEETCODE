
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 


# starting from the beginning

def lengthOfLastWord(self, s):
        tmp = 0
        counting = False
        for i in range(len(s)):
            if s[i] == ' ' and counting == True:
                counting = False
            elif s[i] != ' '  and counting == True :
                tmp += 1 
            elif s[i] != ' ' and counting == False:
                tmp = 1
                counting = True
        
        return tmp

# starting from the end 

def lengthOfLastWord(self, s):
        n = len(s) -1
        tmp = 0
        counting = False
        while(n >= 0):
            if s[n] == ' ' and counting == True :
                break
            elif s[n] != ' ' and counting == False :
                tmp = 1
                n -= 1
                counting = True
            elif s[n] != ' ' and counting == True :
                tmp += 1
                n -= 1
            else :
                n -= 1
            
        return  tmp