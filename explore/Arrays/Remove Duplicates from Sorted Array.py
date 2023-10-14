class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        return list(set(sorted(nums)))
    
nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution.removeDuplicates(nums))