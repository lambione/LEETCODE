# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


def plusOne(self, digits):
        number = 0
        n = len(digits) - 1
        # use powers of ten to recreate the number in a variable
        for i in range(len(digits)):
            if n > 0:
                number += (10 ** n) * digits[i] 
                n -= 1
            else :
                number += digits[i]
        # add 1
        number += 1

        # now recreate the array 
        newNumber = str(number)
        newArr = []
        for j in range(len(newNumber)):
            newArr.append(int(newNumber[j]))
        
        return newArr
