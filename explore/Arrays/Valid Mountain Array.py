class Solution(object):
    @staticmethod
    def validMountainArray(arr: list) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]: return False

        roadToUp = True
        elBefore = arr[0]

        for el in arr[1:]:
            if roadToUp:
                if el < elBefore:
                    roadToUp = False
            else:
                if el > elBefore: return False
            
            if elBefore == el:
                return False
                    
            elBefore = el

        if roadToUp: return False

        return True

            
    
arr = [0,3,2,1]

print(Solution.validMountainArray(arr))