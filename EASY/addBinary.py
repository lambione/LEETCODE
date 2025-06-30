# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"



def DecimalToBinary(num):
    arr = []
    while(num > 0):
        arr.append(str(num % 2))
        num = num // 2
    return arr

def BinaryToDecimal(s):
    num = 0
    power = 0
    for i in range(len(s) - 1,-1,-1):
        if s[i] == '1' :
            num += 1 * (2**power)
            power += 1
        else :
            power += 1
    return num

def ReverseList(x):
    s = ""
    for i in range(len(x) - 1,-1,-1):
        s += x[i]
    return s

    
def addBinary(a, b):
    aNormal = BinaryToDecimal(a)
    bNormal = BinaryToDecimal(b)

    summ = aNormal + bNormal 
    if summ == 0 :
        return "0"
    x = DecimalToBinary(summ) 
    xFinal = ReverseList(x)
    return xFinal

print(addBinary("11","1"))



# this is damn

def addBinary(self, a, b):
        sum = int(a, 2)+int(b, 2)
        return bin(sum).replace('0b', '')
