# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#prices = [3,2,6,5,0,3]
#prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
#prices = [3,7,1,6]
# prices = [3,4,1,7]

#naive - O(n^2)
def find_min_max(prices):
    profit = 0
    for i in range(len(prices)):
        #consider each i as selling price for eles to left
        #consider each i as cost price for eles to its right
        hash_profit = []
        for j in range(len(prices)):
            if j <= i:
                hash_profit.append(prices[i]-prices[j])
            else:
                hash_profit.append(prices[j]-prices[i])
        temp = max(hash_profit)
        if profit < temp:
            profit = temp
    
    return profit

def find_max_profit(prices):
    max_stock_price = prices[len(prices)-1]; max_profit = 0
    for i in range(len(prices)-2, 0, -1):
        if prices[i] > max_stock_price:
            max_stock_price = prices[i]
        if max_profit < max_stock_price - prices[i]:
            max_profit = max_stock_price - prices[i]

    return max_profit
        

    
print(find_max_profit(prices))


