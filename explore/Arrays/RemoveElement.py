class Solution(object):
    def removeElement(self, nums, val):
        for el in nums:
            print(el)
            if el == val:
                nums.remove(val)

        return len(nums)
    
    
sol = Solution()
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))