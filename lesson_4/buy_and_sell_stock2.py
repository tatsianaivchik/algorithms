# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).
# Example: prices = [7,1,5,3,6,4] Return: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

def buy_and_sell_stock(prices):
    max_value = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            max_value = max_value + prices[i + 1] - prices[i]

        return max_value

test_prices = [7, 1, 5, 3, 6, 4]  # Return: 7

print(buy_and_sell_stock(test_prices))