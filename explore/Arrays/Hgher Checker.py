class Solution(object):
    @staticmethod
    def heightChecker(heights):
        counter_of_bad_order = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                counter_of_bad_order += 1

        return counter_of_bad_order
        

heights = [1,1,4,2,1,3]
print(Solution.heightChecker(heights))