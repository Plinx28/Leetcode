class Solution(object):
    def countSubstrings(self, s):
        counter = 0
        for j in range(len(s)):
            for i in range(j+1, len(s)+1):
                checking_palindrome = s[j:i]
                print(checking_palindrome)
                if checking_palindrome == checking_palindrome[::-1]:
                    counter +=1
        
        return counter
sol = Solution()
st = 'aabbazaz'
print(sol.countSubstrings(st))