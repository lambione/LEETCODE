# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.



# Complexity here sucks 
def mySqrt1(x):
    num = 1
    while( num*num != x and num * num < x): 
        num += 1
    
    if(num*num != x):
        return num - 1
    else:
        return num


# O(log(n)*n) rivisited
def mySqrt2(x):
    cop = x // 2
    flag = False
    while(True):
        if cop*cop == x :
            return cop
        elif cop*cop > x:
            if flag == True:
                return cop - 1
            else :
                cop = cop // 2
        elif cop*cop < x :
            cop += 1
            flag = True
    return cop

#log(N)
def mySqrt3(x):
    def mySqrt(self, x):
        start = 0
        end = x
        mid = (start + end) // 2
        while(start <= end):
            mid = (start + end ) // 2
            if mid*mid == x :
                return mid
            elif mid*mid > x:
                end = mid -1
            elif mid*mid < x :
                start = mid + 1
    
        # we want the precise value rounded down
        if mid*mid > x :
            return mid - 1
        else :
            return mid

print(mySqrt3(8))
