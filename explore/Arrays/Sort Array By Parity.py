class Solution(object):
    @staticmethod
    def sortArrayByParity(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return(nums)

        
nums = [1,4,5,9,14,5,7,4,2,0]

print(Solution.sortArrayByParity(nums))