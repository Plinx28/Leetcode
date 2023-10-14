class Solution(object):

    @classmethod
    def sortedSquares(cls, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([num*num for num in nums])

print(Solution.sortedSquares([-7,-3,2,3,11]))