from collections import deque

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        expected = deque(matrix[0])

        for row in matrix[1:]:
            expected.pop()
            expected.appendleft(row[0])

            for j in range(1, len(row)):
                if row[j] != expected[j]:
                    return False
    
        return True       


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
sol = Solution()
print(sol.isToeplitzMatrix(matrix))