class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        if len(prices)==0 or len(prices)==1:
            return max_profit    
        left=0
        right=1      
        while left<=right and right<len(prices):
            if prices[right]-prices[left]>0:
                max_profit=max(max_profit,prices[right]-prices[left])
                right+=1
            else:
                left=right
                right+=1

        return max_profit  