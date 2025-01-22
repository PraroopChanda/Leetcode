class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        if len(prices)==0 or len(prices)==1:
            return max_profit    
        left=0
        right=1      
        sell_price=0
        buy_price=0      
        while left<=right and right<len(prices):
            sell_price=prices[right]
            buy_price=prices[left]
            if sell_price-buy_price>=0:
                max_profit=max(max_profit,sell_price-buy_price)
                right+=1
            else:
                left=right
                right+=1

        return max_profit  