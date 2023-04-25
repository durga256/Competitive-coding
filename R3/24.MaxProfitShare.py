import sys
price = [10, 22, 5, 75, 65, 80]
#price = [2, 30, 15, 10, 8, 25, 80]
#price = [100, 30, 15, 10, 8, 25, 80]
#price = [90, 80, 70, 60, 50]
#price = [7,2,4,8,7]

def max_prof(low,high):
    max_stock_price = price[high]; max_profit = 0
    for i in range(high,low-1,-1):
        if max_stock_price < price[i]:
            max_stock_price = price[i]
        if max_profit < max_stock_price - price[i]:
            max_profit = max_stock_price - price[i]
    return max_profit


def find_profits():
    max_profit = 0
    n = len(price); temp = []
    for i in range(n):
        a,b = max_prof(0,i), max_prof(i+1,n-1)
        temp.append(a+b)
        print(temp)
        max_profit = max(a+b, max_profit)
    print(max_profit)

def find_profit_ptr():
    first_buy = second_buy = -sys.maxsize
    first_sell = second_sell = 0
    for i in range(len(price)):
        first_buy = max(first_buy, -1*price[i])
        first_sell = max(first_sell, first_buy + price[i])
        second_buy = max(second_buy, first_sell - price[i])
        second_sell = max(second_sell, second_buy + price[i])
    
    return second_sell


print(find_profit_ptr())

                    



