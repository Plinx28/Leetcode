import collections
import re
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        current_longer = ''
        longer = ''
        for l in s:
            if l in t:
                t = re.sub(l, '', t)
                





sol = Solution()
s = 'ADOBECODEBANC'
t = "ABC"

# Output: "BANC"
print(sol.minWindow(s, t))
        