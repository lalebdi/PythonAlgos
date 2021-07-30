"""
Problem:
 Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made
 from buying on one day and selling on another day.
"""
arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# Brute force:
# Time complexity: O(n^2)
# Space complexity: O(1)
def buy_and_sell_once(arr):
    max_profit = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
    return max_profit

# print(buy_and_sell_once(arr))



# Time complexity: O(n)
# Space complexity: O(1)
def buy_and_sell_once(arr):
    max_profit = 0
    min_price = arr[0]

    for price in arr:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit


print(buy_and_sell_once(arr))