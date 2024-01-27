class Solution:
    def twoSum_bruteforce(self, nums, target):
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i,j]


nums = [2,7,11,15]
target = 13

nums = [3,2,4]
target = 6

print(Solution().twoSum_bruteforce(nums, target))