class Solution(object):

    @staticmethod
    def duplicateZeros(arr):
        # arrStart = list(arr)
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0: 
                arr.insert(i, 0)
                arr.pop()


a = [0,1,7,6,0,2,0,7]
print(*a)
Solution.duplicateZeros(a)
print(*a)



        