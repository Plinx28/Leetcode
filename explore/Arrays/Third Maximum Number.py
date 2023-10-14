class Solution(object):
    @staticmethod
    def thirdMax(nums):
        # try:
        #     first_max = max(nums)
        #     for _ in range(nums.count(first_max)):
        #         nums.remove(first_max)

        #     second_max = max(nums)
        #     for _ in range(nums.count(second_max)):
        #         nums.remove(second_max)

        #     return max(nums)
        # except:
        #     return first_max
        nums_sorted = sorted(set(nums))
        if len(nums_sorted) > 2:
            return nums_sorted[-3]
        else:
            return nums_sorted[-1]

nums = [-1,2,3]
print(Solution.thirdMax(nums))
print(sorted(nums))