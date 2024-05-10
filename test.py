def smallest_number(all_prices):
    min = all_prices[0]
    for item in all_prices:
      if min > item:
        min = item
      return min