# class Solution:
#     @staticmethod
#     def maxSubArray(nums: list[int]) -> int:
#         """Given an integer array nums, find the subarray with the largest sum, and return its sum."""
#         if len(nums) == 0:
#             return 0

#         maxCurrentSum = nums[0]

#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 currentSum = sum(nums[i:j+1])

#                 if currentSum > maxCurrentSum:
#                     maxCurrentSum = currentSum
                
#         return maxCurrentSum
    


class Solution:
    @staticmethod
    def maxSubArray(nums):
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution.maxSubArray(nums))
