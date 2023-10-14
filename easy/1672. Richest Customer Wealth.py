class Solution(object):
    def maximumWealth(self, accounts):
        maxWealth = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > maxWealth:
                maxWealth = wealth

        return maxWealth
    
sol = Solution()
accounts = [[1,5],[7,3],[3,5]]

print(sol.maximumWealth(accounts))