class Solution(object):
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return sorted(set(nums)) != sorted(nums)
    

a = [1,5,-2,-4,0,0]
print(a)
print(sorted(a))
print(list(set(a)))
print(Solution.containsDuplicate(a))