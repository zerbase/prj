class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = []
        
        dp.append(cost[0])
        dp.append(cost[1])
        
        for i in range(2, len(cost)):
            dp.append(min(dp[i-2], dp[i-1]) + cost[i])
            
        return min(dp[len(cost)-2],dp[len(cost)-1])
