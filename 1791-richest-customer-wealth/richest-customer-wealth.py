class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richness=[]
        for i in range(0,len(accounts)):
            richness.append(sum(accounts[i]))
        return max(richness)
        