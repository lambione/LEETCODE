# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

def singleNumber(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else :
            del dic[num]

    print(list(dic.keys())[0])
    return list(dic.keys())[0]

singleNumber([4,1,2,1,2])