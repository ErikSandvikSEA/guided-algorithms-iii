# returns the max profit that can be made from a single buy n sell
# you have to buy before selling

# bitcoin_prices = [1050, 270, 1540, 3800, 2]
# find_max_profit(bitcoin_prices) // should return 3530

# 1.) Run through examples
# 2.) Ask questions as a way to inform a checklist of tasks that need to be handled

bitcoin_prices = [10, 2, 7, 5, 8, 11, 9]
# max profit we can make her is buying at 5 and selling at 11 -> 6


def find_max_profit(prices):
    # find the largest differences in the values and toss out any differences that result from shorting (selling before buying)

    # if the first index is the largest value, then our profit is 0

    if len(prices) < 1:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


print(find_max_profit(bitcoin_prices))
