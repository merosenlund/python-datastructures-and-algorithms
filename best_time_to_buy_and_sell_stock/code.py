def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    buy = 0
    sell = 1
    while buy < len(prices) - 1:
        profit = prices[sell] - prices[buy]
        if profit > max_profit:
            max_profit = profit
            sell += 1
        elif profit < 0:
            buy += 1
        else:
            if sell < len(prices) - 1:
                sell += 1
            else:
                buy += 1
    return max_profit