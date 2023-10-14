class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for letter in set(ransomNote):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
    

sol = Solution()
ransomNote = 'aabbea'
magazine = 'kkkmcaakmjb;lba'
print(sol.canConstruct(ransomNote, magazine))