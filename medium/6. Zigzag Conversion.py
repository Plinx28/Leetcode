class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows == 0:
            return s
        new_word = ['' for _ in range(numRows)]
        range_list = [i for i in range(numRows)]
        while len(range_list) < len(s):
            for i in range_list[::-1][1:]:
                range_list.append(i)
                if len(range_list) >= len(s):
                    break

        for symbol, i in zip(s, range_list):
            new_word[i] = new_word[i] + symbol
        
        return ''.join(new_word)

sol = Solution()
print(sol.convert("PAYPALISHIRING", numRows = 4))