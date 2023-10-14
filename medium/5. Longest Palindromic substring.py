class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        
        longest_substring = ''

        for j in range(len(s)):
            if len(longest_substring) > len(s[j:]):
                return longest_substring
            for i in range(j+1, len(s)+1):
                checking_palindrome = s[j:i]
                if checking_palindrome == checking_palindrome[::-1] and len(checking_palindrome) > len(longest_substring):
                    longest_substring = checking_palindrome
                
        return longest_substring


sol = Solution()
s = "babad"
s_1 = 'abbbcbbb'

print(f'Result: {sol.longestPalindrome("cbbd")}')
