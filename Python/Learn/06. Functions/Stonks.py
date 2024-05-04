stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
  max_p = 0
  for i in range(a, b + 1):
    max_p = max(max_p, price_at(i))
  return max_p

def min_price(a, b):
  min_p = price_at(a)
  for i in range(a, b + 1):
    min_p = min(min_p, price_at(i))
  return min_p

print(price_at(5))
print(max_price(1, 10))
print(min_price(7, 20))