# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
prices = [7,1,5,3,6,4]

def bestTimeToSell():
    max_stock_price = prices[len(prices)-1]; max_profit = 0
    for i in range(len(prices)-2, -1, -1):
        if prices[i] > max_stock_price:
            max_stock_price = prices[i]
        if max_stock_price - prices[i] > max_profit:
            max_profit = max_stock_price - prices[i]
    
    return max_profit


print(bestTimeToSell())

