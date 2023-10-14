class Solution(object):
    @staticmethod
    def checkIfExist(arr):
        for el in arr:
            if arr.count(0) > 1: return True
            if el * 2 in arr and el != 0: return True
            
        return False
        

arr = [0, 0]
print(Solution.checkIfExist(arr))