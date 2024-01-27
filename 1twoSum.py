class Solution:
    def twoSum_bruteforce(self, nums, target):
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i,j]

    def twoSum(self, nums, target):
        hashIndex = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashIndex:
                return [hashIndex[diff], i]
            hashIndex[n] = i

# Testing 
nums = [2,7,11,15]
target = 9

nums = [3,3] 
target = 6

nums = [3,2,4]
target = 6

print(Solution().twoSum_bruteforce(nums, target))

print(Solution().twoSum(nums, target))