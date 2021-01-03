# Brute Force
# O(N^2)
def maxProfit1(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


print(maxProfit1([7, 1, 5, 3, 6, 4]))  # answer = 5
print(maxProfit1([7, 6, 4, 3, 1]))  # answer = 0

# One Pass
# O(N)
"""
Iterates over prices and check if price is less than the current
min_price, if so swap. Checks if price - min_price is greater than
the current max_profit, if so swap.
"""


def maxProfit2(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


print(maxProfit2([7, 1, 5, 3, 6, 4]))  # answer = 5
print(maxProfit2([7, 6, 4, 3, 1]))  # answer = 0
