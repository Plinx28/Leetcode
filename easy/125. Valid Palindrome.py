class Solution(object):
    def isPalindrome(self, s):
        import re
        s = s.lower()
        s = re.sub(r'\W|_','', s)

        if s == s[::-1]:
            return True
        else:
            return False
    
string = 'A man, a plan, a canal: Panama'
sol = Solution()

print(sol.isPalindrome(string))
