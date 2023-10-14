class Solution(object):
    def isValid(self, s):
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False
        else:
            while len(s) != 0:
                if "()" in s:
                    s = s.replace("()","")   
                elif "{}" in s: 
                    s = s.replace("{}","")
                elif "[]" in s:
                    s = s.replace("[]","")
                else:
                    return False
        return True

                
solut = Solution()

print(solut.isValid('{(})'))