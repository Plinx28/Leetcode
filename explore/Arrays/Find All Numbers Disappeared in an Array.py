'''Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.'''


class Solution(object):
    @staticmethod
    def findDisappearedNumbers(nums: list[int]) -> list[int] | list[None]:
        if len(nums) == 0:
            return nums
        unic_nums = set(nums)
        return [el for el in range(1, len(nums)+1) if el not in unic_nums]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums_sorted = [1, 2, 2, 3, 3, 4, 7, 8]
# need to return [5, 6]
print(Solution.findDisappearedNumbers(nums))
