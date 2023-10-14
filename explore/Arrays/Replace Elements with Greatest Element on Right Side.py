class Solution(object):
    @staticmethod
    def replaceElements(arr, mx = -1):
        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])

        return arr
        
arr = [17,1]
print(Solution.replaceElements(arr))
arr_2 = [17,18,5,4,6,1]
print(Solution.replaceElements(arr_2))