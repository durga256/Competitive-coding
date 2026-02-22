import sys
price = [10, 22, 5, 75, 65, 80]
def find_profit():
    first_buy = second_buy = -sys.maxsize
    first_sell = second_sell = 0
    for i in range(len(price)):
        first_buy = max(first_buy, -1*price[i])
        first_sell = max(first_sell, first_buy+price[i])
        second_buy = max(second_buy, first_sell - price[i])
        second_sell = max(second_sell, second_buy + price[i])
        print(first_buy, first_sell, second_buy, second_sell)
    print(second_sell)

find_profit()