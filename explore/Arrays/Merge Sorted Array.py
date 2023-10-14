class Solution(object):
    @staticmethod
    def merge(nums1, m, nums2, n):
        for _ in range(len(nums1) - m):
            nums1.pop()

        nums1.extend(nums2[:n])
        nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution.merge(nums1, m, nums2, n)
print(nums1)