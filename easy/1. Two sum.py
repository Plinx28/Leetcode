class Solution():
    def twoSum(self, nums, target):
        index_value = {}
        for i in range(len(nums)):
            if target - nums[i] in index_value:
                return [index_value[target - nums[i]], i]
            index_value[nums[i]] = i
                
# Easy to use known value (target) to find solution
solution = Solution()

print(solution.twoSum(nums=[0, 3, 3], target=6))