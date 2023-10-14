class Solution(object):
    @staticmethod
    def removeElement(nums, val):
        [nums.remove(val) for _ in range(nums.count(val))]
        return len(nums)
    

nums = [0,1,2,2,3,0,4,2]
value = 2

print(Solution.removeElement(nums, value))