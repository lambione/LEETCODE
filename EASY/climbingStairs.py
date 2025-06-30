


def climbStairs(n):
        # edge cases
        if n == 1 :
            return 1
        elif n == 2 :
            return 2
        elif n == 3:
            return 3
        else :
            # start with one on the counter which is the all 1's
            num = 1 
            availability = n-1 #how many 2's I've transformed
            if (n % 2) == 0:
                num += 1 #all 2's
                
            while(availability > (n // 2)):
                num += availability
                availability -= 1
            
            return num

print(climbStairs(5))

