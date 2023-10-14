class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False
        if t > s:
            s, t = t, s
        for i in ''.join(set(s)):
            if s.count(i) != t.count(i):
                return False
        return True

sol = Solution()
s = 'anagram'
t = 'nagaram'
print(sol.isAnagram(s, t))
