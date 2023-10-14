class Solution(object):
    def groupAnagrams(self, strs):
        groups_list = []
        symbols_dict = {}
        for word in strs:
            sorted_symbols = ''.join(sorted(word))
            if sorted_symbols in symbols_dict:
                symbols_dict[sorted_symbols].append(word)
            else:
                symbols_dict[sorted_symbols] = [word]

        for symbols_kit in symbols_dict:
            groups_list.append(symbols_dict[symbols_kit])
            
        return groups_list

            
sol = Solution()
strs_1 = ["eat","tea","tan","ate","nat","zzz"]
strs_2 = ["cab","pug","pei","nay","ron","rae","ems","ida","mes"]
print(sol.groupAnagrams(strs=strs_1))