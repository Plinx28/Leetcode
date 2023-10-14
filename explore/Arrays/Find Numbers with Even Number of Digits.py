class Solution(object):
    def findNumbers(self, nums):
        return sum([1 if len(str(el)) % 2 == 0 else 0 for el in nums])
                
sol = Solution()
nums = [12, 345, 2, 6, 7896]

print(sol.findNumbers(nums))