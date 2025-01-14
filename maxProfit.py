from typing import List
def maxProfit(prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        #if price is higher tha previuos day 
        if prices[i] > prices[i-1]:
            #add the price difference to profit 
            profit += prices[i] - prices[i-1]
    return profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))