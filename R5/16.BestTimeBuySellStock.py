prices = [7,1,5,3,6,4]

def best_time():
    n = len(prices)
    max_day = prices[n-1]; result = 0
    for i in range(n-2,-1,-1):
        if prices[i] > max_day:
            max_day = prices[i]
        if result < max_day - prices[i]:
            result = max_day - prices[i]

    print(result)

best_time()
