# from itertools import accumulate
# class Solution(object):
#     def runningSum(self, nums):
#         return list(accumulate(nums))
    
# class Solution(object):
#     def runningSum(self, nums):
#         numsLen = len(nums)
#         accumulitedList = []
#         def accumulite(summorizedValue=0, counter=0):
#             if numsLen != counter:
#                 summorizedValue += nums[counter]
#                 counter += 1
#                 accumulitedList.append(summorizedValue)
#                 accumulite(summorizedValue, counter)
#             else:
#                 return summorizedValue
#         accumulite()
#         return accumulitedList

class Solution(object):
    def runningSum(self, nums):
        # summorizedList = []
        # currentSum = 0
        # for el in nums:
        #     currentSum += el
        #     summorizedList.append(currentSum)

        # return summorizedList

        return [sum(nums[:i+1]) for i in range(len(nums))]
sol = Solution()
nums = [1,2,3,4,5]
print(sol.runningSum(nums))