class Solution(object):
    def lengthOfLongestSubstring(self, s):
        current_longer = ''
        longer = ''
        for i in s:
            if i not in current_longer:
                current_longer = current_longer + i
            else:
                for s_index in range(len(current_longer)+1):
                    if i not in current_longer[s_index:]:
                        current_longer = current_longer[s_index:] + i
                        break
                          
            if len(current_longer) > len(longer):
                longer = current_longer
            
        return len(longer)


sol = Solution()
s1 = 'pwwkew'
print(f'Result {s1}: {sol.lengthOfLongestSubstring(s1)}')
s ='Привет'
print(s[0:0+1])