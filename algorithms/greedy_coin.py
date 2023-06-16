def make_change(target_amount, coin_denominations):
    # Sort the coin denominations in descending order
    coin_denominations.sort(reverse=True)

    # Initialize a counter for counting the number of coins used
    coin_count = 0

    for coin in coin_denominations:
        # Count the number of coins needed for the current denomination
        num_coins = target_amount // coin
        coin_count += num_coins

        # Update the remaining target amount
        target_amount -= num_coins * coin

    return coin_count

# Example usage:
coin_denominations = [25, 10, 5, 1]
target_amount = 67

minimum_coins = make_change(target_amount, coin_denominations)
print("Minimum number of coins needed:", minimum_coins)
